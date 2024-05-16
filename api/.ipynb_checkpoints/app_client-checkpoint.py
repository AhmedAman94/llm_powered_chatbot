import requests
import streamlit as st                                      # Turns scripts into shareable web apps

# Function to get response from GPT 3.5 API
def get_openai_response(input_text):
    response = requests.post("http://localhost:8000/openai/invoke",
                             json={'input': {'topic': input_text}})
    try:
        return response.json()['output']

    except KeyError:
        return ("Error processing the response, please check the API server.", response.json())
         

# Function to get response from Llama 3 API
def get_llama3_response(input_text):
    response = requests.post("http://localhost:8000/llama3/invoke",
                             json={'input': {'topic': input_text}})
    try:
        return response.json()['output']
        
    except KeyError:
        return ("Error processing the response, please check the API server.", response.json())
    
# Streamlit UI
st.title('LangChain Demo with GPT 3.5 & Llama 3 API')
input_text_openai = st.text_input("Enter your query for GPT 3.5:")
input_text_llama3 = st.text_input("Enter your query for Llama 3:")

if input_text_openai:
    st.write(get_openai_response(input_text_openai))

if input_text_llama3:
    st.write(get_llama3_response(input_text_llama3))

