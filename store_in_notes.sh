#!/bin/bash

# Check if the correct number of arguments are provided
if [ "$#" -ne 2 ]; then
    echo "Usage: ./store_in_notes.sh <transcription_file_path> <summary_file_path>"
    exit 1
fi

# Get file paths from arguments
TRANSCRIPTION_FILE_PATH="$1"
SUMMARY_FILE_PATH="$2"

# Extract file name without extension to use as note title
VIDEO_TITLE=$(basename "$TRANSCRIPTION_FILE_PATH")
VIDEO_TITLE="${VIDEO_TITLE%.*}"  # Remove file extension

# Read the transcription and summary content
if [ -f "$TRANSCRIPTION_FILE_PATH" ] && [ -f "$SUMMARY_FILE_PATH" ]; then
    TRANSCRIPTION=$(cat "$TRANSCRIPTION_FILE_PATH")
    SUMMARY=$(cat "$SUMMARY_FILE_PATH")
    
    # Create note content with summary and transcription
    NOTE_CONTENT="Summary: \n\n Summary: $SUMMARY\n\n Full Transcription\n\n$TRANSCRIPTION"
    
    # Create an Apple Note with both summary and transcription
    osascript -e "tell application \"Notes\" to make new note at folder \"Notes\" with properties {name:\"$VIDEO_TITLE\", body:\"$NOTE_CONTENT\"}"
    
    echo "Note added to Apple Notes with title: $VIDEO_TITLE"
else
    echo "Error: Could not find transcription or summary file."
    exit 1
fi
