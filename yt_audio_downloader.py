import yt_dlp
import sys
import os

def download_audio(youtube_url, output_dir):
    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Define yt-dlp options for audio download in WebM format
    ydl_opts = {
        'format': 'bestaudio/best',              # Download the best available audio quality
        'postprocessors': [
            {
                'key': 'FFmpegExtractAudio',     # Use FFmpeg to extract audio
                'preferredcodec': 'webm',        # Convert to WebM format
                'preferredquality': '16',       # Set audio quality to 16 kbps
            }
        ],
        'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),  # Output file template
        'noplaylist': True,                     # Ensure only a single video is downloaded (no playlists)
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"Downloading audio from: {youtube_url}")
            ydl.download([youtube_url])
        print("Download completed successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    # Ensure correct arguments are provided
    if len(sys.argv) < 3:
        print("Usage: python download_audio.py <youtube_url> <output_dir>")
        sys.exit(1)
    
    youtube_url = sys.argv[1]
    output_dir = sys.argv[2]

    # Call the download_audio function
    download_audio(youtube_url, output_dir)

if __name__ == "__main__":
    main()
