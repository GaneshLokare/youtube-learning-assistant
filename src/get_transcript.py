from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import urlparse, parse_qs

class Transcript:
    def __init__(self, url):
        """
        Initialize the Transcript object with a URL
        """
        self.url = url
        self.video_id = self.get_video_id(url)
        self.transcript_data = self.get_transcript()
        self.text = self.get_text() if self.transcript_data else None

    def get_video_id(self, url):
        """
        Extract video ID from YouTube URL
        Works with various YouTube URL formats
        """
        parsed_url = urlparse(url)
        if parsed_url.hostname == 'youtu.be':
            return parsed_url.path[1:]
        if parsed_url.hostname in ('www.youtube.com', 'youtube.com'):
            if parsed_url.path == '/watch':
                return parse_qs(parsed_url.query)['v'][0]
        raise ValueError('Invalid YouTube URL')

    def get_transcript(self, language='en'):
        """
        Get transcript from YouTube video
        Parameters:
            language (str): Language code (default: 'en' for English)
        Returns:
            list: List of transcript dictionaries with text and timestamps
        """
        try:
            transcript = YouTubeTranscriptApi.get_transcript(self.video_id, languages=[language])
            return transcript
        except Exception as e:
            print(f"Error getting transcript: {str(e)}")
            return None

    def get_text(self):
        """
        Get transcript text without timestamps
        Returns:
            str: Complete transcript text
        """
        if not self.transcript_data:
            return None
        
        return ' '.join(entry['text'] for entry in self.transcript_data)

    def print_formatted_transcript(self):
        """
        Print transcript in a readable format with timestamps
        """
        if not self.transcript_data:
            print("No transcript available")
            return
        
        full_text = ' '.join(entry['text'] for entry in self.transcript_data)
        return full_text

# # Example usage
# if __name__ == "__main__":
#     video_url = input("Enter YouTube video URL: ")
    
#     try:
#         # Create Transcript object
#         transcript = Transcript(video_url)
        
#         transcript.print_formatted_transcript()
        
#     except Exception as e:
#         print(f"Error: {str(e)}")