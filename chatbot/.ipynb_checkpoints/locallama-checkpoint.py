from langchain_openai import ChatOpenAI                     # LLM used to power chatbot
from langchain_core.prompts import ChatPromptTemplate       # Use to create flexible templated prompts for chat models
from langchain_core.output_parsers import StrOutputParser   # OutputParser that parses LLMResult into the top likely string
from langchain_community.llms import Ollama                 # Used for third party integrations and open source LLMs

import streamlit as st                                      # Turns scripts into shareable web apps
from dotenv import load_dotenv                              # Loads environment variables from a .env file into process.env
import os

load_dotenv()

# Accessing the environment variables
os.environ["LANGCHAIN_API_KEY"]    = os.getenv("LANGCHAIN_API_KEY")   # To use LangSmith tracking
os.environ["LANGCHAIN_TRACING_V2"] = "true"                           # To use LangSmith tracking

# Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Respond to user queries"),
        ("user", "Question:{question}")
    ]
)

# Streamlit Framework
st.title('Langchain Demo with Llama 3 API')
input_text    = st.text_input("Search the topic you want")

# ollama Llamma3 LLM
llm           = Ollama(model = "llama3")
output_parser = StrOutputParser()
chain         = prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))