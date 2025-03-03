import os
import sys
import subprocess
import argparse
from yt_audio_downloader import download_audio
from audio_transcription import main as transcribe_audio
from summarize import main as summarize_text

def youtube_to_text(youtube_url, output_dir, save_to_notes=False):
    # Step 1: Download audio
    print("Step 1: Downloading audio from YouTube...")
    download_audio(youtube_url, output_dir)

    # Find the downloaded audio file
    audio_files = [f for f in os.listdir(output_dir) if f.endswith('.webm')]
    if not audio_files:
        print("Error: No audio file was downloaded")
        sys.exit(1)

    audio_file = os.path.join(output_dir, audio_files[0])
    transcription_path = os.path.join(output_dir, os.path.splitext(audio_files[0])[0] + '.txt')

    # Step 2: Transcribe the audio
    print("\nStep 2: Transcribing audio to text...")
    sys.argv = ['', audio_file, transcription_path]
    transcribe_audio()

    # Step 3: Summarize the transcription
    print("\nStep 3: Generating summary...")
    sys.argv = ['', transcription_path]
    summary_path = summarize_text()

    # Step 4: Store in Apple Notes (if enabled)
    if save_to_notes:
        print("\nStep 4: Storing in Apple Notes...")
        store_notes_script = os.path.join(os.path.dirname(__file__), "store_in_notes.sh")
        subprocess.run(['bash', store_notes_script, transcription_path, str(summary_path)])
    else:
        print("\nSkipping Apple Notes storage as requested")

    print(f"\nProcess completed!")
    print(f"Audio file: {audio_file}")
    print(f"Transcription: {transcription_path}")
    print(f"Summary: {summary_path}")

def main():
    parser = argparse.ArgumentParser(description='Download YouTube video, transcribe audio, and optionally save to Apple Notes')
    parser.add_argument('youtube_url', help='URL of the YouTube video')
    parser.add_argument('output_dir', help='Directory to save output files')
    parser.add_argument('--no-notes', action='store_true', help='Skip saving to Apple Notes')
    
    args = parser.parse_args()

    # Create output directory if it doesn't exist
    if not os.path.exists(args.output_dir):
        os.makedirs(args.output_dir)

    youtube_to_text(args.youtube_url, args.output_dir, not args.no_notes)

if __name__ == "__main__":
    main() 