"""
Parallel Video Renderer - Streamlit Application
Main application entry point
"""

import os
import multiprocessing
import streamlit as st
import pandas as pd

from video_processor import VideoProcessor
from charts import create_comparison_chart, create_speedup_visualization, create_segment_timeline
from styles import get_custom_css


# Page configuration
st.set_page_config(
    page_title="Parallel Video Renderer",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Apply custom CSS
st.markdown(get_custom_css(), unsafe_allow_html=True)


def render_header():
    """Render application header"""
    st.markdown(
        "<h1 style='text-align: center; font-size: 2.5rem; margin-bottom: 0;'>"
        "PARALLEL VIDEO RENDERING</h1>",
        unsafe_allow_html=True
    )
    st.markdown(
        "<p style='text-align: center; font-size: 1rem; color: #888888; margin-top: 0.5rem;'>"
        "Distributed Processing Pipeline Visualization</p>",
        unsafe_allow_html=True
    )
    st.markdown("---")


def render_sidebar():
    """
    Render sidebar with settings and info
    
    Returns:
        int: Selected segment duration
    """
    with st.sidebar:
        st.markdown("## ⚙️ SETTINGS")
        st.markdown("---")
        
        segment_duration = st.slider(
            "Segment Duration (seconds)",
            min_value=1,
            max_value=30,
            value=10,
            help="Duration of each video segment"
        )
        
        st.markdown("---")
        st.markdown("### 💻 SYSTEM INFO")
        cpu_cores = multiprocessing.cpu_count()
        st.metric("CPU Cores", cpu_cores)
        
        st.markdown("---")
        st.markdown("### 📊 FEATURES")
        st.markdown("""
        • Split videos into segments  
        • Sequential processing  
        • Parallel processing  
        • Performance comparison  
        • Grayscale conversion  
        """)
    
    return segment_duration


def render_file_upload():
    """
    Render file upload section
    
    Returns:
        UploadedFile: Uploaded video file or None
    """
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 📁 VIDEO UPLOAD")
        uploaded_file = st.file_uploader(
            "Choose a video file",
            type=['mp4', 'avi', 'mov', 'mkv', 'flv', 'wmv', 'webm'],
            help="Upload a video file to process",
            label_visibility="collapsed"
        )
    
    with col2:
        if uploaded_file:
            st.markdown("### ℹ️ FILE INFO")
            file_size_mb = uploaded_file.size / (1024 * 1024)
            st.metric("File Size", f"{file_size_mb:.2f} MB")
            st.metric("Format", uploaded_file.name.split('.')[-1].upper())
    
    return uploaded_file


def render_performance_metrics(seq_time, par_time, workers, num_segments):
    """
    Render performance metrics section
    
    Args:
        seq_time (float): Sequential processing time
        par_time (float): Parallel processing time
        workers (int): Number of CPU workers used
        num_segments (int): Number of video segments
    """
    speedup = seq_time / par_time if par_time > 0 else 0
    time_saved = seq_time - par_time
    percent_faster = (time_saved / seq_time * 100) if seq_time > 0 else 0
    
    # First metrics row
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("SEQUENTIAL TIME", f"{seq_time:.2f}s")
    
    with col2:
        st.metric("PARALLEL TIME", f"{par_time:.2f}s", delta=f"-{time_saved:.2f}s")
    
    with col3:
        st.metric("SPEEDUP FACTOR", f"{speedup:.2f}x", delta=f"{percent_faster:.1f}% faster")
    
    with col4:
        st.metric("SEGMENTS", num_segments)
    
    # Second metrics row
    st.markdown("")
    col5, col6, col7, col8 = st.columns(4)
    
    with col5:
        st.metric("TIME SAVED", f"{time_saved:.2f}s")
    
    with col6:
        efficiency = (speedup / workers * 100) if workers > 0 else 0
        st.metric("EFFICIENCY GAIN", f"{int(efficiency)}%")
    
    with col7:
        st.metric("CPU CORES", f"{workers}")
    
    with col8:
        st.metric("TOTAL SEGMENTS", f"{num_segments}")


def render_performance_charts(seq_time, par_time, speedup):
    """
    Render performance visualization charts
    
    Args:
        seq_time (float): Sequential processing time
        par_time (float): Parallel processing time
        speedup (float): Speedup factor
    """
    st.markdown("---")
    
    chart_col1, chart_col2 = st.columns(2)
    
    with chart_col1:
        st.markdown("### PROCESSING TIME COMPARISON")
        st.plotly_chart(create_comparison_chart(seq_time, par_time), use_container_width=True)
    
    with chart_col2:
        st.markdown("### TIME DISTRIBUTION")
        st.plotly_chart(create_speedup_visualization(speedup), use_container_width=True)


def render_performance_table(seq_time, par_time, workers, num_segments, speedup):
    """
    Render detailed performance statistics table
    
    Args:
        seq_time (float): Sequential processing time
        par_time (float): Parallel processing time
        workers (int): Number of workers used
        num_segments (int): Number of segments
        speedup (float): Speedup factor
    """
    st.markdown("### 📈 DETAILED STATISTICS")
    
    perf_data = {
        'Metric': [
            'Processing Method',
            'Time (seconds)',
            'Time per Segment',
            'CPU Cores Used',
            'Efficiency'
        ],
        'Sequential': [
            'One by One',
            f'{seq_time:.2f}s',
            f'{seq_time/num_segments:.2f}s',
            '1',
            '100%'
        ],
        'Parallel': [
            'Simultaneous',
            f'{par_time:.2f}s',
            f'{par_time/num_segments:.2f}s',
            str(workers),
            f'{(speedup/workers)*100:.1f}%'
        ]
    }
    
    df = pd.DataFrame(perf_data)
    st.dataframe(df, use_container_width=True, hide_index=True)


def render_output_preview(duration, final_output):
    """
    Render output preview and download section
    
    Args:
        duration (float): Video duration in seconds
        final_output (str): Path to final output file
    """
    st.markdown("---")
    st.markdown("### 💾 OUTPUT PREVIEW")
    
    download_col1, download_col2 = st.columns([1, 2])
    
    with download_col1:
        if os.path.exists(final_output):
            st.markdown(f"""
            <div style='text-align: center; padding: 40px; background: rgba(0,20,0,0.3); 
                        border: 1px solid rgba(0,255,0,0.15); border-radius: 12px;'>
                <div style='font-size: 3rem; margin-bottom: 10px;'>📹</div>
                <p style='color: #888; font-size: 0.9rem;'>output/final_rendered.mp4</p>
                <p style='color: #666; font-size: 0.8rem;'>Duration: {duration:.2f}s</p>
            </div>
            """, unsafe_allow_html=True)
    
    with download_col2:
        if os.path.exists(final_output):
            with open(final_output, "rb") as file:
                st.download_button(
                    label="⬇️ DOWNLOAD PROCESSED VIDEO",
                    data=file,
                    file_name="processed_video.mp4",
                    mime="video/mp4",
                    use_container_width=True
                )
            st.markdown("<br>", unsafe_allow_html=True)
            st.button("▶️ PREVIEW OUTPUT", use_container_width=True, disabled=True)


def render_performance_insights(speedup, time_saved, percent_faster):
    """
    Render performance insights and interpretation
    
    Args:
        speedup (float): Speedup factor
        time_saved (float): Time saved in seconds
        percent_faster (float): Percentage improvement
    """
    st.markdown("---")
    st.markdown("### 💡 PERFORMANCE INSIGHTS")
    
    if speedup > 1.5:
        st.success(f"""
        🎉 **Excellent Performance!**
        
        Parallel processing was **{speedup:.2f}x faster**, saving **{time_saved:.2f} seconds** 
        ({percent_faster:.1f}% improvement).
        This demonstrates the power of utilizing multiple CPU cores for video processing tasks!
        """)
    elif speedup > 1:
        st.info(f"""
        👍 **Good Performance**
        
        Parallel processing was **{speedup:.2f}x faster**, saving **{time_saved:.2f} seconds**.
        The speedup could be improved with longer videos or more segments.
        """)
    else:
        st.warning(f"""
        ⚠️ **Limited Speedup**
        
        Parallel processing showed minimal improvement (speedup: {speedup:.2f}x).
        This typically happens when:
        - The video is very short
        - There aren't enough segments to parallelize effectively
        - Process overhead outweighs the benefits
        
        Try with a longer video (60+ seconds) for better results!
        """)


def render_landing_page():
    """Render landing page when no video is uploaded"""
    st.markdown("---")
    
    # Action buttons
    button_col1, button_col2 = st.columns(2)
    
    with button_col1:
        st.button("🔍 View Pipeline ⚡", use_container_width=True, disabled=True)
    
    with button_col2:
        st.button("📊 Performance Analytics 📈", use_container_width=True, disabled=True)
    
    st.markdown("---")
    
    # Info cards
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div style='background: rgba(0,20,0,0.3); backdrop-filter: blur(20px); 
                    border: 1px solid rgba(0,255,0,0.15); border-radius: 12px; padding: 30px; 
                    text-align: center; height: 200px; display: flex; flex-direction: column; 
                    justify-content: center;'>
            <h3 style='color: #ffffff; margin-bottom: 15px;'>VIDEO INFORMATION</h3>
            <p style='color: #888888; font-size: 0.9rem;'>
                Upload a video to see duration, segments created, and processing details
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style='background: rgba(0,20,0,0.3); backdrop-filter: blur(20px); 
                    border: 1px solid rgba(0,255,0,0.15); border-radius: 12px; padding: 30px; 
                    text-align: center; height: 200px; display: flex; flex-direction: column; 
                    justify-content: center;'>
            <h3 style='color: #ffffff; margin-bottom: 15px;'>SEQUENTIAL TIME</h3>
            <p style='color: #888888; font-size: 0.9rem;'>
                Process segments one by one to establish a baseline performance metric
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div style='background: rgba(0,20,0,0.3); backdrop-filter: blur(20px); 
                    border: 1px solid rgba(0,255,0,0.15); border-radius: 12px; padding: 30px; 
                    text-align: center; height: 200px; display: flex; flex-direction: column; 
                    justify-content: center;'>
            <h3 style='color: #ffffff; margin-bottom: 15px;'>PARALLEL TIME</h3>
            <p style='color: #888888; font-size: 0.9rem;'>
                Leverage multiple CPU cores for simultaneous processing acceleration
            </p>
        </div>
        """, unsafe_allow_html=True)


def main():
    """Main application function"""
    render_header()
    
    segment_duration = render_sidebar()
    uploaded_file = render_file_upload()
    
    if uploaded_file is not None:
        # Save uploaded file
        video_path = f"temp_{uploaded_file.name}"
        with open(video_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        st.success(f"✅ Video uploaded: {uploaded_file.name}")
        
        # Process button
        if st.button("🚀 START PROCESSING", use_container_width=True):
            try:
                processor = VideoProcessor(segment_duration)
                
                # Step 1: Split video
                st.markdown("---")
                st.markdown("### 🔪 STEP 1: SPLITTING VIDEO")
                split_progress = st.progress(0)
                split_status = st.empty()
                
                segments, duration = processor.split_video(
                    video_path,
                    lambda p: split_progress.progress(p)
                )
                
                split_status.success(f"✅ Split into {len(segments)} segments ({duration:.2f}s total)")
                st.plotly_chart(create_segment_timeline(len(segments)), use_container_width=True)
                
                # Step 2: Sequential processing
                st.markdown("### ⏳ STEP 2: SEQUENTIAL PROCESSING")
                seq_progress = st.progress(0)
                seq_status = st.empty()
                
                seq_results, seq_time = processor.process_sequential(
                    segments,
                    lambda p: seq_progress.progress(p)
                )
                
                seq_status.success(f"✅ Sequential processing completed in {seq_time:.2f}s")
                
                # Step 3: Parallel processing
                st.markdown("### ⚡ STEP 3: PARALLEL PROCESSING")
                par_progress = st.progress(0)
                par_status = st.empty()
                
                par_results, par_time, workers = processor.process_parallel(
                    segments,
                    lambda p: par_progress.progress(p)
                )
                
                par_status.success(f"✅ Parallel processing completed in {par_time:.2f}s using {workers} cores")
                
                # Step 4: Stitch video
                st.markdown("### 🔗 STEP 4: STITCHING FINAL VIDEO")
                stitch_progress = st.progress(0)
                final_output = "final_output.mp4"
                
                with st.spinner("Merging segments..."):
                    processor.stitch_segments(par_results, final_output)
                    stitch_progress.progress(1.0)
                
                st.success("✅ Final video created!")
                
                # Performance Analytics
                st.markdown("---")
                st.markdown("## 📊 PERFORMANCE ANALYTICS")
                st.markdown(
                    "<p style='color: #888888; margin-top: -10px;'>"
                    "Detailed metrics from the parallel rendering pipeline</p>",
                    unsafe_allow_html=True
                )
                
                # Calculate metrics
                speedup = seq_time / par_time if par_time > 0 else 0
                time_saved = seq_time - par_time
                percent_faster = (time_saved / seq_time * 100) if seq_time > 0 else 0
                
                # Render all sections
                render_performance_metrics(seq_time, par_time, workers, len(segments))
                render_performance_charts(seq_time, par_time, speedup)
                render_performance_table(seq_time, par_time, workers, len(segments), speedup)
                render_output_preview(duration, final_output)
                render_performance_insights(speedup, time_saved, percent_faster)
                
            except Exception as e:
                st.error(f"❌ Error during processing: {str(e)}")
                st.exception(e)
    else:
        render_landing_page()


if __name__ == "__main__":
    main()
