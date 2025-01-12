from get_transcript import Transcript
from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain_openai import ChatOpenAI


class GenerateQA:
    def __init__(self):
        # self.yt = Transcript(url)
        # self.yt_transcript = self.yt.print_formatted_transcript()
        # Load environment variables from .env
        load_dotenv()
        # Create a ChatOpenAI model
        model = ChatOpenAI(model="gpt-4o-mini", response_format={ "type": "json_object" })

        # Define prompt templates (no need for separate Runnable chains)
        prompt_template = ChatPromptTemplate.from_messages(
            [
                ("system", "You are an advanced AI assistant specialized in processing and analyzing transcripts."),
                ("human", """ You are an AI designed to analyze YouTube video transcripts and generate insightful questions and answers. Below is the transcript of a YouTube video. Your task is to:

                Extract key information and generate Q&A pairs (e.g., questions to test understanding or to dive deeper).
                Provide clear and concise answers to these questions, based on the content of the transcript.
                 
                Guidelines: 
                 
                Each Q&A pair must have exactly two fields: "question" and "answer".

                Focus on the main topics discussed in the video.

                Create a mix of factual, conceptual, and application-based questions.

                Ensure each question has a corresponding, accurate answer derived from the transcript.
                 
                You must ALWAYS respond with a JSON object containing an array of Q&A pairs.
                 
                Return ONLY a JSON object with the specified format.

                Example format:
                {{
                    "qa_pairs": [
                        {{
                            "question": "What is the main topic discussed?",
                            "answer": "The answer to the first question"
                        }},
                        {{
                            "question": "What are the key points mentioned?",
                            "answer": "The answer to the second question"
                        }}
                    ]
                }}

                

                Transcript:
                {transcript}"""),
            ]
        )

        # Create the combined chain using LangChain Expression Language (LCEL)
        self.chain = prompt_template | model | StrOutputParser()
        # chain = prompt_template | model

    def qa_chain(self, yt_transcript):
        # Run the chain
        result = self.chain.invoke({"transcript": yt_transcript})

        # Output
        return result
