# 🚀 Quick Start Guide

Get up and running with Parallel Video Renderer in 5 minutes!

## ⚡ Fast Setup

### 1. Extract the Project
```bash
unzip parallel-video-renderer.zip
cd parallel-video-renderer
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Install FFmpeg

**Ubuntu/Debian:**
```bash
sudo apt update && sudo apt install ffmpeg
```

**macOS:**
```bash
brew install ffmpeg
```

**Windows:**
- Download from https://ffmpeg.org/download.html
- Add to system PATH

### 4. Run the App
```bash
streamlit run app.py
```

Your browser will open at `http://localhost:8501` 🎉

## 📹 First Video Processing

1. **Upload**: Click the upload area and select a video file
2. **Settings**: Adjust segment duration if needed (10s default is fine)
3. **Process**: Click "START PROCESSING" button
4. **Wait**: Watch the progress bars as it processes
5. **Download**: Get your grayscale video!

## 💡 Pro Tips

- **Better Results**: Use videos 30+ seconds long
- **Faster Processing**: Close other applications
- **More Segments**: Decrease segment duration for more parallelization
- **System Info**: Check sidebar to see your CPU core count

## 🎯 Example Videos to Try

Start with:
- **Short test**: 30-60 second video (quick results)
- **Medium**: 2-3 minute video (see real speedup)
- **Long**: 5+ minute video (maximum performance difference)

## ❓ Common Issues

**"ModuleNotFoundError"**
```bash
pip install -r requirements.txt
```

**"FFmpeg not found"**
- Make sure FFmpeg is installed and in PATH
- Restart terminal after installation

**App won't start**
```bash
streamlit run app.py --server.port 8502
```

## 📁 Project Files

- `app.py` - Main application (run this!)
- `video_processor.py` - Core processing logic
- `charts.py` - Visualizations
- `styles.py` - UI styling
- `requirements.txt` - Dependencies

## 🎨 Customization

Want to change the theme? Edit `styles.py`:
- Line 20-25: Background colors
- Line 70-85: Button colors
- Line 180-200: Chart colors

## 📊 Understanding Results

- **Sequential Time**: Baseline processing time
- **Parallel Time**: Accelerated processing time
- **Speedup Factor**: How much faster (2x, 3x, etc.)
- **Efficiency**: How well CPU cores are used

## 🎓 Next Steps

- Read the full [README.md](README.md)
- Check [CONTRIBUTING.md](CONTRIBUTING.md) to contribute
- Experiment with different videos
- Share your results!

---

**Need help?** Open an issue on GitHub or check the documentation.

Happy Processing! 🎬✨
