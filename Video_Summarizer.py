import subprocess
import whisper
from transformers import pipeline
import os
import sys

def extract_audio(video_path, audio_path):
    # Extract audio using ffmpeg
    cmd = ["ffmpeg", "-y", "-i", video_path, "-q:a", "0", "-map", "a", audio_path]
    subprocess.run(cmd, check=True)
    print(f"Audio extracted to {audio_path}")

def transcribe_audio(audio_path, model_size="small"):
    print("Loading Whisper model...")
    model = whisper.load_model(model_size)
    print(f"Transcribing audio file: {audio_path}")
    result = model.transcribe(audio_path, verbose=True)
    print("Transcription complete.")
    return result['text']

def summarize_text(text):
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    max_chunk = 1000
    text_chunks = [text[i:i+max_chunk] for i in range(0, len(text), max_chunk)]
    summary = ""
    for chunk in text_chunks:
        out = summarizer(chunk, max_length=150, min_length=30, do_sample=False)
        summary += out[0]['summary_text'] + " "
    return summary

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 video_summarizer.py video/video_file.mp4")
        sys.exit(1)

    video_path = sys.argv[1]
    
    # Get base name of video (without extension)
    base_name = os.path.splitext(os.path.basename(video_path))[0]

    # Define folder paths
    audio_dir = "audio"
    transcript_dir = "transcript"
    summary_dir = "summary"

    # Create folders if they don't exist
    os.makedirs(audio_dir, exist_ok=True)
    os.makedirs(transcript_dir, exist_ok=True)
    os.makedirs(summary_dir, exist_ok=True)

    # Paths for outputs
    audio_path = os.path.join(audio_dir, f"{base_name}_audio.wav")
    transcript_path = os.path.join(transcript_dir, f"{base_name}_transcript.txt")
    summary_path = os.path.join(summary_dir, f"{base_name}_summary.txt")

    # Step 1: Extract audio
    extract_audio(video_path, audio_path)

    # Step 2: Transcribe audio
    transcript = transcribe_audio(audio_path)

    # Step 3: Save transcript
    with open(transcript_path, "w") as f:
        f.write(transcript)
    print(f"Transcript saved to {transcript_path}")

    # Step 4: Summarize transcript
    summary = summarize_text(transcript)

    # Step 5: Save summary
    with open(summary_path, "w") as f:
        f.write(summary)
    print(f"Summary saved to {summary_path}")

    # Final print (optional)
    print("\nTranscript Preview:\n", transcript[:500], "...")
    print("\nSummary Preview:\n", summary[:500], "...")

# command to run : python3 summarizer.py Anomaly_Detection_PoC.mp4
