from flask import Flask, render_template, request, jsonify
from youtube_transcript_api import YouTubeTranscriptApi
from dotenv import load_dotenv
import os
import google.generativeai as genai

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

app = Flask(__name__)

prompt = """You are a YouTube video transcript summarizer AI. Your job is to take the transcript of a video and summarize it into concise, bullet-point notes. The notes should:
1. Cover the key points discussed in the video.
2. Highlight important details and avoid unnecessary repetition.
3. Be written in simple, clear, and professional language.

Summarize the following transcript in less than 400 words:
"""


# Function to extract transcript
def extract_transcript(youtube_url):
    try:
        if "v=" in youtube_url:
            video_id = youtube_url.split("v=")[1].split("&")[0]
        elif "youtu.be/" in youtube_url:
            video_id = youtube_url.split("youtu.be/")[1]
        else:
            raise ValueError("Invalid YouTube URL format.")
        transcript_data = YouTubeTranscriptApi.get_transcript(video_id)
        transcript = " ".join([item["text"] for item in transcript_data])
        return transcript
    except Exception as e:
        raise e

# Function to summarize transcript
def summarize_transcript(transcript):
    try:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(prompt + transcript)
        return response.text
    except Exception as e:
        raise e

# Route for UI
@app.route('/')
def index():
    return render_template('index.html')

# API Route for summarization
@app.route('/summarize', methods=['POST'])
def summarize():
    try:
        youtube_url = request.form.get("youtube_url")
        if not youtube_url:
            return jsonify({"error": "YouTube URL is required"}), 400
        transcript = extract_transcript(youtube_url)
        summary = summarize_transcript(transcript)
        return jsonify({"transcript": transcript, "summary": summary}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
