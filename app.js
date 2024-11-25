document.getElementById('summarizer-form').addEventListener('submit', async (event) => {
    event.preventDefault();

    const youtubeUrl = document.getElementById('youtube-url').value;
    const loadingElement = document.getElementById('loading');
    const summaryElement = document.getElementById('summary');
    const transcriptElement = document.getElementById('transcript');

    // Show loading indicator
    loadingElement.style.display = 'block';
    summaryElement.innerText = '';
    transcriptElement.innerText = '';

    try {
        const formData = new FormData();
        formData.append('youtube_url', youtubeUrl);

        const response = await fetch('/summarize', {
            method: 'POST',
            body: formData
        });

        if (!response.ok) {
            throw new Error('Failed to summarize the video.');
        }

        const data = await response.json();
        summaryElement.innerText = data.summary;
        transcriptElement.innerText = data.transcript;
    } catch (error) {
        summaryElement.innerText = `Error: ${error.message}`;
    } finally {
        loadingElement.style.display = 'none';
    }
});