# Detailed Usage Guide

## Getting Started

### 1. Opening the Tool

Simply open `video_cropper.html` in any modern web browser:
- Chrome (recommended)
- Firefox
- Safari
- Edge

### 2. Loading a Video

Click the "Select Video File" button and choose your video. Supported formats:
- MP4 (recommended)
- WebM
- OGG
- Most browser-supported video formats

### 3. Navigating Your Video

**Playback Controls:**
- Click the play/pause button to control playback
- Use the timeline slider to jump to any position
- Current time and total duration are displayed below the slider

**Tips:**
- Play the video to find your desired start point
- Pause when you reach it for precise selection
- Use the slider for quick navigation

### 4. Selecting Time Range

**Setting Start Point:**
1. Navigate to where you want the clip to start
2. Click "Set Start Point"
3. The tool will automatically suggest an end point 2 minutes later

**Setting End Point:**
1. Navigate to where you want the clip to end
2. Click "Set End Point"
3. Or keep the auto-suggested end point

**Duration Display:**
- Shows the selected segment duration
- Warns if duration exceeds 2 minutes (if that's your target)
- Displays the time range (start → end)

### 5. Generating Crop Commands

Click "Get Crop Instructions" to download a text file containing:
- FFmpeg command (fast, recommended)
- Python/moviepy alternative
- Detailed instructions

### 6. Cropping the Video

#### Using FFmpeg (Fast Method):

```bash
cd /path/to/your/videos
ffmpeg -i "input.mp4" -ss START_TIME -t DURATION -c copy "output.mp4"
```

**Example:**
```bash
ffmpeg -i "2025-11-06_17.42.20_normal.mp4" -ss 659.65 -t 21.23 -c copy "cropped_output.mp4"
```

#### Using Python (Alternative):

```python
from moviepy.editor import VideoFileClip

video = VideoFileClip("input.mp4")
cropped = video.subclip(START_TIME, END_TIME)
cropped.write_videofile("output.mp4")
```

## Advanced Features

### Batch Processing Multiple Videos

Create a script to process multiple videos:

```bash
#!/bin/bash
for video in *.mp4; do
    ffmpeg -i "$video" -ss 600 -t 120 -c copy "cropped_$video"
done
```

### Custom Duration

Want a different duration than 2 minutes? Just adjust the end point manually.

### Frame-Accurate Cropping

For frame-perfect accuracy (slower):

```bash
ffmpeg -ss START -i input.mp4 -t DURATION -c copy output.mp4
```

Moving `-ss` before `-i` makes seeking more accurate but slower.

## Common Issues

### Issue: Video Won't Load
**Solution:** Ensure the video format is browser-compatible. Convert if needed:
```bash
ffmpeg -i input.avi -c:v libx264 -c:a aac output.mp4
```

### Issue: Cropped Video Starts at Wrong Time
**Solution:** Use accurate seeking mode or remove `-c copy` to re-encode:
```bash
ffmpeg -i input.mp4 -ss 600 -t 120 output.mp4
```

### Issue: File Size is Large
**Solution:** The tool uses stream copy for speed. To compress:
```bash
ffmpeg -i input.mp4 -ss 600 -t 120 -c:v libx264 -crf 23 output.mp4
```

## Tips & Tricks

1. **Preview First**: Always play through the section before cropping
2. **Use Keyboard**: Space bar often controls play/pause in browsers
3. **Multiple Attempts**: You can load the same video multiple times to create different clips
4. **Organize Output**: Create a separate folder for cropped videos
5. **Backup Originals**: Never overwrite original files

## Performance Notes

- **Browser**: Modern Chrome/Firefox recommended for best performance
- **FFmpeg with -c copy**: Fastest method, completes in seconds
- **Python moviepy**: Slower but more flexible, good for additional processing
- **Large Files**: Tool works with videos of any size, limited only by browser memory

## Keyboard Shortcuts (Browser-dependent)

- `Space`: Play/Pause (in most browsers)
- `Arrow Keys`: Fine-tune timeline position
- `F11`: Fullscreen (helpful for long videos)
