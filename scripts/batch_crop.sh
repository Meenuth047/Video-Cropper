#!/bin/bash
# Batch crop multiple videos with the same time range

# Configuration
START_TIME=600    # Start at 10 minutes
DURATION=120      # 2 minutes duration

# Check if FFmpeg is installed
if ! command -v ffmpeg &> /dev/null; then
    echo "Error: FFmpeg is not installed"
    exit 1
fi

# Process all MP4 files in current directory
for video in *.mp4; do
    # Skip if no files found
    [ -e "$video" ] || continue
    
    # Skip already cropped files
    if [[ $video == cropped_* ]]; then
        echo "Skipping already cropped file: $video"
        continue
    fi
    
    output="cropped_${video}"
    
    echo "Processing: $video"
    ffmpeg -i "$video" -ss $START_TIME -t $DURATION -c copy "$output" -y
    
    if [ $? -eq 0 ]; then
        echo "✓ Successfully created: $output"
    else
        echo "✗ Failed to process: $video"
    fi
done

echo "Batch processing complete!"
