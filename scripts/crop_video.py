#!/usr/bin/env python3
"""
Simple command-line video cropper using moviepy
"""

from moviepy.editor import VideoFileClip
import argparse
import sys
import os

def format_time(seconds):
    """Convert seconds to MM:SS format"""
    mins = int(seconds // 60)
    secs = int(seconds % 60)
    return f"{mins:02d}:{secs:02d}"

def crop_video(args):
    """Crop video based on arguments"""
    
    # Check input file exists
    if not os.path.exists(args.input):
        print(f"Error: Input file '{args.input}' not found")
        sys.exit(1)
    
    try:
        print(f"Loading: {args.input}")
        video = VideoFileClip(args.input)
        
        # Get video duration
        duration = video.duration
        print(f"Video duration: {format_time(duration)}")
        
        # Validate times
        if args.start >= duration:
            print(f"Error: Start time ({args.start}s) exceeds video duration")
            sys.exit(1)
        
        if args.end > duration:
            print(f"Warning: End time exceeds duration, using video end")
            args.end = duration
        
        if args.start >= args.end:
            print("Error: Start time must be before end time")
            sys.exit(1)
        
        # Crop video
        crop_duration = args.end - args.start
        print(f"Cropping: {format_time(args.start)} → {format_time(args.end)}")
        print(f"Duration: {format_time(crop_duration)}")
        
        cropped = video.subclip(args.start, args.end)
        
        # Write output
        print(f"Writing: {args.output}")
        cropped.write_videofile(
            args.output,
            codec='libx264',
            audio_codec='aac',
            verbose=False,
            logger=None if args.quiet else 'bar'
        )
        
        print("✓ Done!")
        
        # Cleanup
        video.close()
        cropped.close()
        
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(
        description='Crop video segments',
        epilog='Example: python crop_video.py input.mp4 -s 600 -e 720 -o output.mp4'
    )
    
    parser.add_argument('input', help='Input video file')
    parser.add_argument('-s', '--start', type=float, required=True,
                        help='Start time in seconds')
    parser.add_argument('-e', '--end', type=float, required=True,
                        help='End time in seconds')
    parser.add_argument('-o', '--output', required=True,
                        help='Output video file')
    parser.add_argument('-q', '--quiet', action='store_true',
                        help='Suppress progress bar')
    
    args = parser.parse_args()
    crop_video(args)

if __name__ == '__main__':
    main()
