# YouTube to Text Transcription & Summarization

A Python-based tool that downloads YouTube videos, transcribes the audio to text using OpenAI's Whisper model, and generates an AI summary using Ollama.

## Features

- Download audio from YouTube videos
- Transcribe audio to text using OpenAI's Whisper model
- Generate AI summaries of transcriptions using Ollama
- Optional integration with Apple Notes for storing results
- MPS (Metal Performance Shaders) acceleration support on macOS

## Requirements

- Python 3.10 (required for Whisper with MPS support on macOS)
- FFmpeg (for audio processing)
- Ollama (for AI summarization)

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/tarkalabs/youtube-video-transcriber.git
   cd youtube-to-text
   ```

2. Create and activate a virtual environment:
   ```
   python3.10 -m venv transcribe
   source transcribe/bin/activate
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Ensure Ollama is installed and running on your system:
   - Visit [Ollama's website](https://ollama.ai/) for installation instructions
   - Pull the required model: `ollama pull llama3.2:2b`

## Usage
```
python youtube_to_text.py "https://www.youtube.com/watch?v=UF8uR6Z6KLc" '~/Desktop/transcribed/'
```
