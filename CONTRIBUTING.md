# Contributing to Parallel Video Renderer

Thank you for your interest in contributing! This document provides guidelines for contributing to the project.

## 🤝 How to Contribute

### Reporting Bugs

If you find a bug, please create an issue with:
- Clear description of the bug
- Steps to reproduce
- Expected vs actual behavior
- Screenshots if applicable
- System information (OS, Python version, etc.)

### Suggesting Enhancements

Enhancement suggestions are welcome! Please:
- Check if the enhancement has already been suggested
- Provide a clear description of the feature
- Explain why it would be useful
- Include examples if possible

### Pull Requests

1. **Fork the repository**
   ```bash
   git clone https://github.com/yourusername/parallel-video-renderer.git
   cd parallel-video-renderer
   ```

2. **Create a branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make your changes**
   - Follow the existing code style
   - Add comments for complex logic
   - Update documentation if needed

4. **Test your changes**
   - Ensure the app runs without errors
   - Test with different video files
   - Verify UI remains responsive

5. **Commit your changes**
   ```bash
   git add .
   git commit -m "Add: your feature description"
   ```

6. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

7. **Create a Pull Request**
   - Provide a clear description
   - Reference any related issues
   - Include screenshots for UI changes

## 📝 Code Style

- Follow PEP 8 guidelines
- Use descriptive variable names
- Add docstrings to functions
- Keep functions focused and modular
- Comment complex algorithms

### Example Function Structure

```python
def process_video(video_path, options):
    """
    Process video with given options
    
    Args:
        video_path (str): Path to video file
        options (dict): Processing options
        
    Returns:
        str: Path to processed video
        
    Raises:
        ValueError: If video_path is invalid
    """
    # Implementation
    pass
```

## 🧪 Testing

Before submitting:
- Test with videos of different lengths
- Test with various file formats
- Verify all UI elements work correctly
- Check performance metrics are accurate

## 📚 Documentation

When adding features:
- Update README.md if needed
- Add inline comments
- Update docstrings
- Include usage examples

## 🎯 Development Setup

1. Install development dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the application:
   ```bash
   streamlit run app.py
   ```

## ✅ Checklist

Before submitting a PR, ensure:
- [ ] Code follows project style
- [ ] All functions have docstrings
- [ ] No unused imports or variables
- [ ] UI changes look good on different screen sizes
- [ ] Application runs without errors
- [ ] Changes are documented

## 🙋 Questions?

Feel free to:
- Open an issue for discussion
- Ask in pull request comments
- Contact the maintainers

Thank you for contributing! 🎉
