import os
from flask import Flask, render_template, request, jsonify
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled
from youtube_transcript_api.formatters import TextFormatter
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

app = Flask(__name__)

# Prompt for summarizing the video transcript
prompt = """You are a YouTube video transcript summarizer AI. Your job is to take the transcript of a video and summarize it into concise, bullet-point notes. The notes should:
1. Cover the key points discussed in the video.
2. Highlight important details and avoid unnecessary repetition.
3. Be written in simple, clear, and professional language.

Summarize the following transcript in less than 400 words:
"""

@app.route('/summary', methods=['GET'])
def summary_api():
    url = request.args.get('url', '')
    if not url:
        return jsonify({"error": "No URL provided"}), 400
    
    try:
        video_id = extract_video_id(url)
        transcript = get_transcript(video_id)
        summary = generate_summary(transcript, prompt)
        return jsonify({"summary": summary}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except TranscriptsDisabled:
        return jsonify({"error": "Transcript is disabled for this video."}), 400
    except Exception as e:
        return jsonify({"error": f"Error generating summary: {str(e)}"}), 500

# Function to extract video ID from the URL
def extract_video_id(youtube_url):
    if "youtube.com" in youtube_url:
        video_id = youtube_url.split("v=")[1]
        if '&' in video_id:  # to handle URLs with additional parameters
            video_id = video_id.split('&')[0]
    elif "youtu.be" in youtube_url:
        video_id = youtube_url.split("/")[-1]
    else:
        raise ValueError("Invalid YouTube URL format.")
    return video_id

# Function to get transcript for the video
def get_transcript(video_id):
    try:
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
        transcript = ' '.join([d['text'] for d in transcript_list])
        return transcript
    except TranscriptsDisabled:
        raise TranscriptsDisabled("Transcript is disabled for this video.")
    except Exception as e:
        raise Exception(f"Error fetching transcript: {str(e)}")

# Function to generate summary using Google Gemini API
def generate_summary(transcript_text, prompt):
    try:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(prompt + transcript_text)
        return response.text
    except Exception as e:
        raise Exception(f"Error in Google Gemini API: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)
