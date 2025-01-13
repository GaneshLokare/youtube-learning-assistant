import gradio as gr
import pandas as pd
from src.get_transcript import Transcript
from src.qa_generate import GenerateQA
from src.summarize import Summarize
import json
import re
import os

def is_valid_youtube_url(url):
    youtube_pattern = r'^(https?://)?(www\.)?(youtube\.com/watch\?v=|youtu\.be/)[A-Za-z0-9_-]+(\?.*)?$'
    return bool(re.match(youtube_pattern, url))

def get_transcript(url):
    if not is_valid_youtube_url(url):
        return None
    try:
        yt = Transcript(url)
        return yt.print_formatted_transcript()
    except Exception as e:
        return None

def generate_summary(url, progress=gr.Progress()):
    try:
        transcript = get_transcript(url)
        if not transcript:
            return "Error: Could not fetch transcript. Please check the URL."
        
        complete_summary = ""
        words = transcript.split()
        # process only approx 5000 words at a time to avoid context window error
        for i in progress.tqdm(range(0, len(words), 5000), desc="Generating Summary"):
            chunk = " ".join(words[i:i+5000])
            summarizer = Summarize()
            chunk_summary = summarizer.summarize_chain(chunk)
            complete_summary += chunk_summary + "\n"
            
        return complete_summary
    except Exception as e:
        return f"Error: {str(e)}"

def generate_qa(url, filename, progress=gr.Progress()):
    try:
        transcript = get_transcript(url)
        if not transcript:
            return None, None, gr.update(visible=False)
        
        df = pd.DataFrame(columns=["question", "answer"])
        words = transcript.split()
        
        for i in progress.tqdm(range(0, len(words), 5000), desc="Generating Q&A Pairs"):
            chunk = " ".join(words[i:i+5000])
            qa_generator = GenerateQA()
            qa_data = qa_generator.qa_chain(chunk)
            parsed_data = json.loads(qa_data)
            df = pd.concat([df, pd.DataFrame(parsed_data["qa_pairs"])], ignore_index=True)
        
        if not filename.endswith('.csv'):
            filename += '.csv'
        df.to_csv(filename, index=False)
        
        return df, os.path.abspath(filename), gr.update(visible=True)
    except Exception as e:
        return None, None, gr.update(visible=False)

# Create Gradio interface
with gr.Blocks() as demo:
    gr.Markdown("# YouTube Content Analysis")
    
    with gr.Row():
        url_input = gr.Textbox(
            label="YouTube URL",
            placeholder="Enter YouTube video URL...",
            lines=1
        )
    
    with gr.Row():
        filename_input = gr.Textbox(
            label="Output CSV Filename (for Q&A pairs)",
            placeholder="Enter filename for the CSV output",
            value="qa_pairs",
            lines=1
        )
    
    with gr.Row():
        with gr.Column():
            summary_btn = gr.Button("Generate Summary", variant="primary")
            summary_output = gr.Textbox(
                label="Video Summary",
                interactive=False,
                lines=10
            )
        
        with gr.Column():
            qa_btn = gr.Button("Generate Q&A", variant="primary")
            output_table = gr.Dataframe(
                headers=["Question", "Answer"],
                label="Generated Q&A Pairs"
            )
            download_btn = gr.File(
                label="Download Q&A CSV",
                visible=False,
                interactive=True
            )
    
    # Summary button handler
    summary_btn.click(
        fn=generate_summary,
        inputs=[url_input],
        outputs=[summary_output]
    )
    
    # Q&A button handler
    qa_btn.click(
        fn=generate_qa,
        inputs=[url_input, filename_input],
        outputs=[
            output_table,
            download_btn,
            download_btn
        ]
    )

if __name__ == "__main__":
    demo.launch()