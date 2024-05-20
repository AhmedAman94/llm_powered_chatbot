from langchain_openai import ChatOpenAI                     # LLM used to power chatbot
from langchain_community.llms import Ollama                 # Used for third party integrations and open source LLMs  
from langchain_core.prompts import ChatPromptTemplate       # Use to create flexible templated prompts for chat models
from fastapi import FastAPI                                 # Used for building APIs in Python
import uvicorn                                              # Used to run asynchronous Python web code using the ASGI specification
from langserve import add_routes                            # Used to deploy LangChain runnables and chains as a REST API
from langchain_core.output_parsers import StrOutputParser   # OutputParser that parses LLMResult into the top likely string
from dotenv import load_dotenv                              # Loads environment variables from a .env file into process.env
import os

load_dotenv()

# Accessing the environment variables
os.environ["OPENAI_API_KEY"]       = os.getenv("OPENAI_API_KEY")      # To access Open AI LLM
os.environ["LANGCHAIN_API_KEY"]    = os.getenv("LANGCHAIN_API_KEY")   # To use LangSmith tracking
os.environ["LANGCHAIN_TRACING_V2"] = "true"                           # To use LangSmith tracking

# Initialize FastAPI app
app = FastAPI(
    title       = "LangChain Server",
    version     = "1.0",
    description = "Base API Server"
)

# @app.get("/")  # Handles requests to the root URL
# async def root():
#     return {"message": "Hello World from FastAPI"}

# Define prompt templates
prompt1 = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Respond to user queries in a succinct way. Give examples or names of companies/ key public individuals where necessary."),
        ("user", "Question:{topic}")
    ]
)

prompt2 = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Respond to user queries in a succinct way. Give examples or names of companies/ key public individuals where necessary."),
        ("user", "Question:{topic}")
    ]
)

# Define models
model_gpt35  = ChatOpenAI(model = "gpt-3.5-turbo")
model_llama3 = Ollama(model = "llama3")

# Define output parser
output_parser = StrOutputParser()

# Define chains
chain1 = prompt1|model_gpt35|output_parser
chain2 = prompt2|model_llama3|output_parser

# Add routes to FastAPI app
add_routes(
    app,
    chain1,
    path = "/openai"
)

# @app.post("/openai")
# async def test_openai():
#     return {"message": "OpenAI endpoint is reachable"}


add_routes(
    app,
    chain2,
    path = "/llama3"
)

# @app.post("/llama3")
# async def test_llama3():
#     return {"message": "Llama3 endpoint is reachable"}


# Start the Uvicorn server
if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)


