
# **Brieflyst**  

**A Chrome extension that automatically retrieves transcripts of YouTube videos and generates concise summaries, saving you time and effort.**  

---

## **Features**
- **Automatic URL Detection**: No need to manually input the video URL; the extension fetches it from the active YouTube tab.
- **AI-Powered Summarization**: Utilizes Google’s Gemini API to create clear, concise, and professional summaries.
- **Seamless Integration**: Works directly within the browser, providing summaries in a popup window.
- **Error Handling**: Notifies users if transcripts are unavailable or disabled for a video.

---

## **Getting Started**
Follow these steps to set up and use the extension locally:

### **Prerequisites**
- Google Chrome browser installed.
- Basic knowledge of running Python scripts and installing packages.

---

### **Installation**
#### **Step 1: Clone the Repository**
```bash
git clone https://github.com/yourusername/youtube-video-transcript-summarizer.git
cd youtube-video-transcript-summarizer
```

#### **Step 2: Set Up the Backend**
1. Install **Python** (version 3.7 or above).
2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the project directory and add your Google API key:
   ```
   GOOGLE_API_KEY=your_google_api_key_here
   ```

#### **Step 3: Run the Backend Server**
Start the Flask server by running:
```bash
python app.py
```
The server will run on `http://127.0.0.1:5000` by default.

#### **Step 4: Set Up the Chrome Extension**
1. Open Chrome and go to `chrome://extensions`.
2. Enable **Developer Mode** using the toggle in the top-right corner.
3. Click **Load Unpacked** and select the `extension` folder from this project.

---

## **How To get Google Gemini API**

-**Create a Google Cloud Project:**

1. Go to <a href="https://console.cloud.google.com/" > Google Cloud Console </a> 
2. If you don't already have a project, click "Select a project" at the top of the page and then "New Project".
3. Give your project a name.
4. Click Create to create the project.

-**Enable Google Gemini API:**
1. After creating your project, go to the <a href="https://aistudio.google.com/" > Google ai studio </a>
2. On This page Click the Get API option and Create an api And Select the project for which u want the api
3. Now paste the API key in .env file as shown above
4. Access Your API in the Google Cloud Console, go to the APIs & Services > Credentials page.

## **Tech Stack**
<a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/javascript/javascript-original.svg" alt="javascript" width="40" height="40"/> </a> 
<a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a>
<a href="https://www.w3.org/html/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original-wordmark.svg" alt="html5" width="40" height="40"/> </a><a href="https://www.w3schools.com/css/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/css3/css3-original-wordmark.svg" alt="css3" width="40" height="40"/> </a> 
<a href="https://flask.palletsprojects.com/en/stable/" target="_blank" rel="noreferrer"> <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTmD38KsMgEwahtWc_Nfs5ZVktP9dBc36MUZA&s" alt="css3" width="40" height="40"/> </a>  

### **How to Use**
1. Open a YouTube video in Chrome.
2. Click on the **YouTube Video Transcript Summarizer** icon in the extensions toolbar.
3. The extension will:
   - Automatically fetch the video URL.
   - Retrieve the transcript using the backend server.
   - Generate a concise summary and display it in the popup.

---


## **Future Enhancements**
1.  **Multilingual Support:**
Add support for transcripts in multiple languages that uses language detection and translate summaries if necessary.

2. **Support for Live Streams:**
It will Continuously update summaries in realtime as the livestream goes on.

3. **Save and Share:**
Let users save the summaries to their local storage or export them as PDFs or text files. 

4. **Voice Summaries:**
Add a text-to-speech feature to convert summaries into audio for users who prefer listening.
---

## **Contributing**
Contributions are welcome! If you’d like to contribute:
1. Fork this repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add a feature"
   ```
4. Push to your branch:
   ```bash
   git push origin feature-name
   ```
5. Submit a pull request.

---



## **Acknowledgments**
- **[YouTube Transcript API](https://pypi.org/project/youtube-transcript-api/)**: For fetching YouTube transcripts.
- **Google Gemini API**: For generating high-quality summaries.
- Special thanks to everyone who supported and inspired this project!

---
