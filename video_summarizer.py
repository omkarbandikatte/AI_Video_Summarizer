from youtube_transcript_api import YouTubeTranscriptApi
import streamlit as st
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROK_API_KEY"))
prompt = """You are a Youtube Video SUmmarizer which summarizers the video transcript in a concise manner and provides key points. and also provide me the important part by highlighting it and also generate questions using the transcripts to prepare for an Exam.
Please provide the summarized text here:-  """

def generate_summary(transcript, prompt):
    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": transcript}
        ]
    )
    return response.choices[0].message.content
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