from get_transcript import Transcript
from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain_openai import ChatOpenAI


class Summarize:
    def __init__(self):
        # self.yt = Transcript(url)
        # self.yt_transcript = self.yt.print_formatted_transcript()
        # Load environment variables from .env
        load_dotenv()
        # Create a ChatOpenAI model
        model = ChatOpenAI(model="gpt-4o-mini")

        # Define prompt templates (no need for separate Runnable chains)
        prompt_template = ChatPromptTemplate.from_messages(
            [
                ("system", "You are an advanced AI assistant specialized in processing and analyzing transcripts."),
                ("human", """ You are an AI expert in text summarization. Your goal is to summarize a YouTube transcript into a detailed yet concise summary.

                    Guidelines:

                    Break the summary into paragraphs for better readability.
                    Include detailed information about the main ideas, examples, or critical data mentioned in the transcript.
                    The output should be easy to read, insightful, and visually engaging for end-users.

                Transcript:
                {transcript}"""),
            ]
        )

        # Create the combined chain using LangChain Expression Language (LCEL)
        self.chain = prompt_template | model | StrOutputParser()
        # chain = prompt_template | model

    def summarize_chain(self, yt_transcript):
        # Run the chain
        result = self.chain.invoke({"transcript": yt_transcript})

        # Output
        return result
