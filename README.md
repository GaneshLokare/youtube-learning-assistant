# youtube-learning-assistant


youtube-learning-assistant is a Python application that automatically generates Q&A pairs and summaries YouTube video, making it easier to learn and review content from educational videos.

## Features

- **YouTube Transcript Processing**: Automatically fetches and processes transcripts from YouTube videos
- **Q&A Generation**: Creates meaningful question-answer pairs from video content
- **Summary Generation**: Produces concise summaries of video content
- **User-Friendly Interface**: Simple Gradio web interface for easy interaction
- **CSV Export**: Export Q&A pairs to CSV format for further use
- **Progress Tracking**: Visual progress bars for long processing tasks
- **Error Handling**: Robust error handling for invalid URLs and processing issues

## Installation

1. Clone the repository:
```bash
git clone https://github.com/GaneshLokare/youtube-learning-assistant.git
cd youtube-learning-assistant
```

2. Create and activate a virtual environment:
```bash
python -m venv youtubenenv
# On Windows
youlearnenv\Scripts\activate
# On Unix or MacOS
source youtubenenv/bin/activate
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

## Usage

1. Open your openai account and create a openai api key.
2. Create a ".env" file and put your openai api key in it.
    - OPENAI_API_KEY = "your_openai_api_key"
3. Start the application:
```bash
python app.py
```

4. Open your web browser and navigate to the local URL shown in the terminal (typically http://127.0.0.1:7860)

5. Enter a YouTube URL in the input field

6. Choose your desired operation:
   - Click "Generate Summary" to get a concise summary of the video
   - Click "Generate Q&A" to create question-answer pairs
   
7. View the results directly in the interface

8. For Q&A pairs, you can download them as a CSV file using the download button

## Project Structure

```
youtube-learning-assistant/                    
├── src/
│    ├── __init__.py
│    ├── get_transcript.py     # YouTube transcript fetching functionality
│    ├── qa_generate.py        # Q&A generation module
│    ├── summarize.py          # Summary generation module
├── app.py                     # Main application file
├── requirements.txt           # Project dependencies
└── README.md                  # Project documentation
```

## Requirements

- Python 3.8 or higher
- Gradio
- langchain
- YouTube Transcript API
- Other dependencies listed in requirements.txt



