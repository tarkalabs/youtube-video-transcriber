import torch
from transformers import pipeline
import sys
import os

def main():
    # Check if input arguments are provided
    if len(sys.argv) < 3:
        print("Usage: python main.py <input_audio_path> <output_txt_path>")
        sys.exit(1)
    
    input_audio_path = sys.argv[1]
    output_txt_path = sys.argv[2]

    # Validate the input file
    if not os.path.exists(input_audio_path):
        print(f"Error: The input file '{input_audio_path}' does not exist.")
        sys.exit(1)

    # Ensure MPS is available, fallback to CPU if not
    device = torch.device("mps") if torch.backends.mps.is_available() else torch.device("cpu")
    print(f"Device set to use: {device.type}")

    chunk_length = float(sys.argv[4]) if len(sys.argv) > 4 else 30.0

    # Load the ASR pipeline with the desired Whisper model
    pipe = pipeline(
        "automatic-speech-recognition",
        model="openai/whisper-base",
        chunk_length_s=chunk_length,
        device=device
    )

    # Transcribe the audio file
    print(f"Transcribing '{input_audio_path}'...")
    transcription = pipe(input_audio_path)["text"]

    # Save the transcription to the output file
    with open(output_txt_path, "w") as output_file:
        output_file.write(transcription)
    print(f"Transcription saved to '{output_txt_path}'")

if __name__ == "__main__":
    main()
