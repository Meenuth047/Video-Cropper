#!/usr/bin/env python3
"""
Example Python script for video cropping using moviepy
"""

from moviepy.editor import VideoFileClip
import sys

def crop_video(input_file, start_time, end_time, output_file):
    """
    Crop a video segment
    
    Args:
        input_file: Path to input video
        start_time: Start time in seconds
        end_time: End time in seconds
        output_file: Path to output video
    """
    try:
        print(f"Loading video: {input_file}")
        video = VideoFileClip(input_file)
        
        print(f"Cropping from {start_time}s to {end_time}s")
        cropped = video.subclip(start_time, end_time)
        
        print(f"Writing output: {output_file}")
        cropped.write_videofile(output_file, codec='libx264', audio_codec='aac')
        
        print("Done!")
        video.close()
        cropped.close()
        
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python crop_video.py <input> <start_time> <end_time> <output>")
        print("Example: python crop_video.py video.mp4 600 720 output.mp4")
        sys.exit(1)
    
    input_file = sys.argv[1]
    start_time = float(sys.argv[2])
    end_time = float(sys.argv[3])
    output_file = sys.argv[4]
    
    crop_video(input_file, start_time, end_time, output_file)
