from youtube_transcript_api import YouTubeTranscriptApi
import streamlit as st
import os
import requests
from dotenv import load_dotenv

load_dotenv()

prompt = """You are a Youtube Video SUmmarizer which summarizers the video transcript in a concise manner and provides key points. and also provide me the important part by highlighting it and also generate questions using the transcripts to prepare for an Exam.
Please provide the summarized text here:-  """

def generate_summary(transcript, prompt):
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")

    if not GROQ_API_KEY:
        return "❌ Error: GROQ_API_KEY not found. Check your .env file or Streamlit secrets."

    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "llama3-70b-8192",
        "messages": [
            {"role": "system", "content": prompt},
            {"role": "user", "content": transcript}
        ],
        "temperature": 0.7,
        "max_tokens": 1000
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"]
        else:
            return f"❌ Groq API Error {response.status_code}: {response.text}"
    except Exception as e:
        return f"❌ Exception occurred: {e}"
    
def extract_transcript(youtube_url):
    try:
        video_id = youtube_url.split("watch?v=")[1]
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        transcript_text = ""
        for i in transcript:
            transcript_text += " "+i["text"]
        return transcript_text
    except Exception as e:
        st.error(f"Error extracting transcript: {e}")
        return None
    

st.title("YouTube Video Summarizer")

youtube_link = st.text_input("Enter YouTube Video URL", key="youtube_url")

if youtube_link:
    video_id = youtube_link.split("=")[1]
    st.image(f"https://img.youtube.com/vi/{video_id}/0.jpg", use_container_width=True)

if st.button("Generate Summary"):
    transcript_text = extract_transcript(youtube_link)

    if transcript_text:
        summary = generate_summary(transcript_text, prompt)
        st.markdown("## Notes:- ")
        st.write(summary)