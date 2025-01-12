# youtube-learning-assistant


YouLearn is a Python application that automatically generates Q&A pairs and summaries from YouTube video transcripts, making it easier to learn and review content from educational videos.

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
2. Create a ".env" file and put your openai api key.
3. Start the application:
```bash
python app.py
```

2. Open your web browser and navigate to the local URL shown in the terminal (typically http://127.0.0.1:7860)

3. Enter a YouTube URL in the input field

4. Choose your desired operation:
   - Click "Generate Summary" to get a concise summary of the video
   - Click "Generate Q&A" to create question-answer pairs
   
5. View the results directly in the interface

6. For Q&A pairs, you can download them as a CSV file using the download button

## Project Structure

```
yyoutube-learning-assistant/
├── app.py                     # Main application file
youtube-learning-assistant
    ├── get_transcript.py     # YouTube transcript fetching functionality
    ├── qa_generate.py        # Q&A generation module
    ├── summarize.py         # Summary generation module
├── requirements.txt        # Project dependencies
└── README.md               # Project documentation
```

## Requirements

- Python 3.8 or higher
- Gradio
- langchain
- YouTube Transcript API
- Other dependencies listed in requirements.txt

## Contributing

1. Fork the repository
2. Create a new branch for your feature
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to Gradio for the web interface framework
- Thanks to YouTube Transcript API for transcript access
- Special thanks to all contributors and users of this project

## Contact

- Create an issue in this repository for bug reports or feature requests
- Submit pull requests for contributing to the project

## Roadmap

Future features and improvements planned:
- Multiple language support
- Batch processing of multiple videos
- Additional export formats
- Custom Q&A templates
- Integration with learning management systems