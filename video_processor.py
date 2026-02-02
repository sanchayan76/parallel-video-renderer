"""
Video Processing Module
Handles video splitting, processing, and merging operations
"""

import os
import time
import shutil
import multiprocessing
from moviepy import VideoFileClip, concatenate_videoclips
from moviepy.video.fx.BlackAndWhite import BlackAndWhite


class VideoProcessor:
    """Main class for video processing operations"""
    
    def __init__(self, segment_duration=10):
        """
        Initialize VideoProcessor
        
        Args:
            segment_duration (int): Duration of each video segment in seconds
        """
        self.segment_duration = segment_duration
        self.segments_dir = "video_segments"
        self.sequential_dir = "processed_sequential"
        self.parallel_dir = "processed_parallel"
    
    def split_video(self, input_path, progress_callback=None):
        """
        Split video into segments
        
        Args:
            input_path (str): Path to input video file
            progress_callback (callable): Optional callback function for progress updates
            
        Returns:
            tuple: (list of segment paths, total video duration)
        """
        video = VideoFileClip(input_path)
        total_duration = video.duration
        
        # Adjust segment duration for short videos
        segment_duration = self.segment_duration
        if total_duration < segment_duration * 2:
            segment_duration = max(1, int(total_duration / 4))
        
        # Clean up and create segments directory
        if os.path.exists(self.segments_dir):
            shutil.rmtree(self.segments_dir)
        os.makedirs(self.segments_dir)
        
        segment_paths = []
        current_time = 0
        segment_num = 0
        total_segments = int(total_duration / segment_duration) + 1
        
        # Split video into segments
        while current_time < total_duration:
            start = current_time
            end = min(current_time + segment_duration, total_duration)
            
            chunk = video.subclipped(start, end)
            output_file = f"{self.segments_dir}/segment_{segment_num:03d}.mp4"
            chunk.write_videofile(output_file, codec='libx264', logger=None)
            
            segment_paths.append(output_file)
            
            if progress_callback:
                progress_callback((segment_num + 1) / total_segments)
            
            segment_num += 1
            current_time = end
        
        video.close()
        return segment_paths, total_duration
    
    @staticmethod
    def apply_grayscale(args):
        """
        Apply grayscale effect to a video segment
        
        Args:
            args (tuple): (input_file_path, output_file_path)
            
        Returns:
            str: Path to processed output file
        """
        input_file, output_file = args
        
        clip = VideoFileClip(input_file)
        bw_clip = clip.with_effects([BlackAndWhite()])
        bw_clip.write_videofile(output_file, codec='libx264', logger=None)
        
        clip.close()
        bw_clip.close()
        
        return output_file
    
    def process_sequential(self, segment_paths, progress_callback=None):
        """
        Process video segments sequentially
        
        Args:
            segment_paths (list): List of segment file paths
            progress_callback (callable): Optional callback for progress updates
            
        Returns:
            tuple: (list of processed segment paths, processing time in seconds)
        """
        # Setup output directory
        if os.path.exists(self.sequential_dir):
            shutil.rmtree(self.sequential_dir)
        os.makedirs(self.sequential_dir)
        
        start = time.time()
        results = []
        
        # Process each segment one by one
        for idx, seg_path in enumerate(segment_paths):
            out_path = f"{self.sequential_dir}/processed_{idx:03d}.mp4"
            self.apply_grayscale((seg_path, out_path))
            results.append(out_path)
            
            if progress_callback:
                progress_callback((idx + 1) / len(segment_paths))
        
        total_time = time.time() - start
        return results, total_time
    
    def process_parallel(self, segment_paths, progress_callback=None):
        """
        Process video segments in parallel using multiprocessing
        
        Args:
            segment_paths (list): List of segment file paths
            progress_callback (callable): Optional callback for progress updates
            
        Returns:
            tuple: (list of processed paths, processing time, number of workers used)
        """
        # Setup output directory
        if os.path.exists(self.parallel_dir):
            shutil.rmtree(self.parallel_dir)
        os.makedirs(self.parallel_dir)
        
        # Prepare jobs
        jobs = []
        for idx, seg_path in enumerate(segment_paths):
            out_path = f"{self.parallel_dir}/processed_{idx:03d}.mp4"
            jobs.append((seg_path, out_path))
        
        # Determine number of workers
        cores = multiprocessing.cpu_count()
        workers = min(cores, len(jobs))
        
        # Process in parallel
        start = time.time()
        
        with multiprocessing.Pool(processes=workers) as pool:
            results = pool.map(self.apply_grayscale, jobs)
        
        total_time = time.time() - start
        
        if progress_callback:
            progress_callback(1.0)
        
        return results, total_time, workers
    
    @staticmethod
    def stitch_segments(segment_paths, output_path):
        """
        Concatenate processed video segments into final output
        
        Args:
            segment_paths (list): List of processed segment paths
            output_path (str): Path for final output video
        """
        clips = [VideoFileClip(p) for p in sorted(segment_paths)]
        final = concatenate_videoclips(clips)
        final.write_videofile(output_path, codec='libx264', logger=None)
        
        # Clean up
        for clip in clips:
            clip.close()
        final.close()
    
    def cleanup(self):
        """Remove temporary directories"""
        dirs_to_remove = [self.segments_dir, self.sequential_dir, self.parallel_dir]
        for directory in dirs_to_remove:
            if os.path.exists(directory):
                shutil.rmtree(directory)
