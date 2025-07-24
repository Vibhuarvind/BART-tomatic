# BART-tomatic
AI-powered video transcription and summarization using Hugging Face’s BART and OpenAI Whisper. Fast, accurate, and organized outputs.

# 🎥 Video Summarizer with Whisper and Transformers

This Python tool automatically **transcribes** and **summarizes** video files using [OpenAI Whisper](https://github.com/openai/whisper) and Hugging Face Transformers.

---

## ✨ Features

- 📼 Extracts audio from `.mp4` videos
- 🧠 Transcribes speech to text with OpenAI's Whisper
- ✍️ Summarizes long transcripts using `facebook/bart-large-cnn`
- 📁 Organized output: audio, transcript, and summary in separate folders
- 🔧 Easy to run locally on macOS/Linux

---

## 📂 Folder Structure
project/
├── video/ # Place your input video files here
│ └── sample_video.mp4
├── audio/ # Auto-generated audio WAV files
│ └── sample_video_audio.wav
├── transcript/ # Auto-generated transcripts
│ └── sample_video_transcript.txt
└── summary/ # Auto-generated summaries
└── sample_video_summary.txt


---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/video-summarizer.git
cd video-summarizer

2. Set up your Python environment
Make sure you're using Python 3.8–3.11.

python3 -m venv .env
source .env/bin/activate
pip install -r requirements.txt
3. Install ffmpeg
Required for audio extraction:

bash
Copy
Edit
# macOS (Homebrew)
brew install ffmpeg

# Ubuntu
sudo apt install ffmpeg
📦 Dependencies
Install these with pip install -r requirements.txt or manually:

txt
Copy
Edit
openai-whisper
transformers
torch
🚀 Usage
Place your video file (e.g. my_video.mp4) in the video/ folder.

Run the summarizer script:

bash
Copy
Edit
python3 video_summarizer.py video/my_video.mp4
Check the following outputs:

audio/my_video_audio.wav

transcript/my_video_transcript.txt

summary/my_video_summary.txt

🧪 Tips for Best Results
Use shorter videos for quick testing.

Use the "tiny" or "base" Whisper model for faster transcription.

Transcripts and summaries are plain text; you can extend to PDF/Markdown export if needed.

🛠 To-Do / Future Enhancements
 Multi-language support

 Batch video processing

 Web interface or Streamlit app

 Timestamped transcripts

📜 License
MIT License. See LICENSE file.

🙌 Credits
Whisper by OpenAI

Transformers by Hugging Face



