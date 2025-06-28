# 🎥 YouTube Video Summarizer using Groq LLM

This Streamlit-based app extracts transcripts from YouTube videos (if available) and uses the **Groq LLM (LLaMA3-70B)** to generate:

- 📄 A concise summary of the video
- ✅ Key takeaways
- 🧠 Highlighted important points
- ❓ Auto-generated questions (exam prep style)

---

## 🚀 Features

- 🔗 Accepts a YouTube video URL
- 📑 Automatically fetches transcript using `youtube-transcript-api`
- 💬 Sends the transcript to Groq API for summarization
- 🎯 Outputs a readable, exam-focused summary with highlights and questions

---

## 🛠️ Tech Stack

| Tool/Library            | Purpose                             |
|-------------------------|-------------------------------------|
| `streamlit`             | Web UI                              |
| `youtube-transcript-api`| Fetching transcripts from YouTube   |
| `groq` API (via `requests`) | Summarizing the transcript using LLaMA3 |
| `python-dotenv`         | Load API keys from `.env` file      |

---

## 📁 Project Structure

video_summarizer/
├── video_summarizer.py # Main Streamlit app
├── requirements.txt # Python dependencies
├── .env # API keys (GROQ_API_KEY)


---

## 📦 Installation

1. **Clone the repository**:
   git clone https://github.com/omkarbandikatte/AI_Video_Summarizer.git
   cd AI_Video_Summarizer

2. **Setting Up Enviornment**:
    python -m venv venv
    source venv/bin/activate 

3. **Install required modules**:
    pip install requirements.txt

4. **Setting GROQ API**:

    GROQ_API_KEY=your_groq_api_key_here

5. **Run the Project**:
    streamlit run video_summarizer.py