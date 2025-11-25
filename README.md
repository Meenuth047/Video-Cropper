# Interactive Video Cropper

A lightweight, browser-based tool for selecting and cropping video segments. Perfect for extracting specific time ranges from long videos without complex video editing software.

![Video Cropper Demo](/Video-Cropper/docs/video-cropping.png)

## Features

- **Visual Selection**: Play video and visually select start/end points
- **Fast Processing**: Uses FFmpeg with stream copy (no re-encoding)
- **Browser-Based**: No installation needed - runs directly in your browser
- **Command Generation**: Automatically generates FFmpeg/Python commands
- **Modern UI**: Clean, intuitive interface with real-time feedback
- **Duration Display**: Shows selected segment duration and warns if exceeds target

## Quick Start

### Method 1: Direct Browser Use (Easiest)

1. Download `video_cropper.html`
2. Double-click to open in your browser
3. Select your video file
4. Choose start/end points
5. Get crop commands

### Method 2: Clone Repository

```bash
git clone https://github.com/meenuth047/video-cropper.git
cd video-cropper
# Open video_cropper.html in your browser
xdg-open video_cropper.html  # Linux
open video_cropper.html      # macOS
start video_cropper.html     # Windows
```

## Prerequisites

To actually crop videos, you need ONE of:

### Option 1: FFmpeg (Recommended - Fastest)
```bash
# Ubuntu/Debian
sudo apt-get install ffmpeg

# macOS
brew install ffmpeg

# Windows
# Download from https://ffmpeg.org/download.html
```

### Option 2: Python with moviepy
```bash
pip install moviepy
```

## Usage

### Step 1: Select Video
Click "Select Video File" and choose your video.

### Step 2: Navigate & Mark Points
- Use play/pause and timeline to navigate
- Click **"Set Start Point"** at desired start time
- Click **"Set End Point"** at desired end time (auto-suggests +2 minutes)

### Step 3: Get Crop Commands
Click **"Get Crop Instructions"** to download commands.

### Step 4: Crop Video
Run the FFmpeg command from the downloaded file:

```bash
ffmpeg -i "input.mp4" -ss 659.65 -t 21.23 -c copy "cropped_output.mp4"
```

Or use Python:
```python
from moviepy.editor import VideoFileClip
video = VideoFileClip("input.mp4")
cropped = video.subclip(659.65, 680.87)
cropped.write_videofile("cropped_output.mp4")
```

## Examples

### Example 1: Extract 2-minute segment
```bash
# Original video: 1 hour long
# Want: Minutes 10:00 to 12:00

ffmpeg -i "long_video.mp4" -ss 600 -t 120 -c copy "excerpt.mp4"
```

### Example 2: Batch crop multiple videos
See `scripts/batch_crop.sh` for batch processing example.

## Advanced Usage

### FFmpeg Parameters Explained

```bash
ffmpeg -i "input.mp4" -ss START -t DURATION -c copy "output.mp4"
```

- `-i`: Input file
- `-ss`: Start time in seconds (e.g., 659.65)
- `-t`: Duration in seconds (e.g., 120 for 2 minutes)
- `-c copy`: Stream copy (no re-encoding, very fast)
- Output filename

### Accurate vs Fast Seeking

**Fast (current method):**
```bash
ffmpeg -i input.mp4 -ss 600 -t 120 -c copy output.mp4
```

**Accurate (slower but frame-perfect):**
```bash
ffmpeg -ss 600 -i input.mp4 -t 120 -c copy output.mp4
```

## Project Structure

```
video-cropper/
├── video_cropper.html      # Main application
├── README.md               # This file
├── docs/
│   ├── demo.png           # Screenshot
│   └── USAGE.md           # Detailed usage guide
├── examples/
│   ├── sample_commands.txt
│   └── python_example.py
└── scripts/
    ├── batch_crop.sh      # Batch processing script
    └── crop_video.py      # Python helper script
```

### FFmpeg not found
```bash
# Check if installed
ffmpeg -version

# If not, install
sudo apt-get install ffmpeg  # Linux
brew install ffmpeg          # macOS
```
