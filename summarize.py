import ollama
from pathlib import Path
import sys

def summarize_text(transcription_path):
    # Read the system prompt and transcription
    system_prompt = Path("system_prompt.txt").read_text(encoding="utf-8")
    transcription = Path(transcription_path).read_text(encoding="utf-8")

    response = ollama.chat(
        model='llama3.2:2b',  #'llama3.2:1b' 'deepseek-r1:7b'
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                'role': 'user',
                'content': transcription
            }
        ]
    )

    return response['message']['content']

def main():
    if len(sys.argv) < 2:
        print("Usage: python summarize.py <transcription_file_path>")
        sys.exit(1)

    transcription_path = sys.argv[1]
    summary = summarize_text(transcription_path)
    
    # Create summary file in same directory as transcription
    summary_path = Path(transcription_path).parent / (Path(transcription_path).stem + "_summary.md")
    summary_path.write_text(summary)
    print(f"Summary saved to: {summary_path}")
    return summary_path

if __name__ == "__main__":
    main()