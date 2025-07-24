
# BART-tomatic

AI-powered video transcription and summarization using Hugging Face’s BART and OpenAI Whisper. Fast, accurate, and organized outputs.

# 🎥 Video Summarizer with Whisper and Transformers

This Python tool automatically **transcribes** and **summarizes** video files using [OpenAI Whisper](https://github.com/openai/whisper) and Hugging Face Transformers.


## ✨ Features

- 📼 Extracts audio from `.mp4` videos  
- 🧠 Transcribes speech to text with OpenAI's Whisper  
- ✍️ Summarizes long transcripts using `facebook/bart-large-cnn`  
- 📁 Organized output: audio, transcript, and summary in separate folders  
- 🔧 Easy to run locally on macOS/Linux  


## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/video-summarizer.git
cd video-summarizer
````

### 2. Set up your Python environment

Make sure you're using Python 3.8–3.11.

```bash
python3 -m venv .env
source .env/bin/activate
pip install -r requirements.txt
```

### 3. Install ffmpeg

Required for audio extraction:

* **macOS (Homebrew):**

```bash
brew install ffmpeg
```

* **Ubuntu:**

```bash
sudo apt install ffmpeg
```

---

## 📦 Dependencies

Install with:

```bash
pip install -r requirements.txt
```

Or manually install:

* openai-whisper
* transformers
* torch

---

## 🚀 Usage

1. Place your video file (e.g. `my_video.mp4`) inside the `video/` folder.

2. Run the summarizer script:

```bash
python3 video_summarizer.py video/my_video.mp4
```

3. Check the generated outputs:

* `audio/my_video_audio.wav`
* `transcript/my_video_transcript.txt`
* `summary/my_video_summary.txt`

---

## 🧪 Tips for Best Results

* Use shorter videos for faster testing.
* Use the "tiny" or "base" Whisper model for faster transcription.
* Transcripts and summaries are saved as plain text — you can extend to PDF or Markdown exports if needed.

---

## 🛠 To-Do / Future Enhancements

* Multi-language support
* Batch video processing
* Web interface or Streamlit app
* Timestamped transcripts

---
