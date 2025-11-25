# importing required packages
from langchain_google_genai import ChatGoogleGenerativeAI
from google.generativeai.types import HarmCategory, HarmBlockThreshold
from dotenv import load_dotenv
import streamlit as st  
import time
import os

# set page configuration
st.set_page_config("AI chatbot", layout = "centered")

# Function for typewriter like animation
def typewriter(text, delay = 0.05):
    """This function generates text generator which prints the AI response as a typewrier"""
    for word in text.split(" "):
        yield word + " "
        time.sleep(delay)

# initializing dotenv file
load_dotenv()
os.environ["GOOGLE_API_KEY"] = os.getenv("GEMINI_API_KEY")
model_name = os.getenv("MODEL")

## LLM configuration with safety settings
llm = ChatGoogleGenerativeAI(
    model = model_name,
    temperature = 0.5,
    safety_settings = {
        HarmCategory.HARM_CATEGORY_HARASSMENT : HarmBlockThreshold.BLOCK_ONLY_HIGH,
        HarmCategory.HARM_CATEGORY_HATE_SPEECH : HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
        HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT : HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
        HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT : HarmBlockThreshold.BLOCK_LOW_AND_ABOVE
    }
)

## initializing the chat session
if "chats" not in st.session_state:
    st.session_state.chats = []
    
## displaying chat messages
for chat in st.session_state.chats:
    with st.chat_message(chat["role"]):
        st.markdown(chat["content"]) 
        
# taking user prompt message
if prompt := st.chat_input("How can i help you ?"):
    with st.chat_message("user"):
        st.markdown(prompt)
        
    # saving the message in chats
    st.session_state.chats.append({"role" : "user", "content" : prompt})
    
    # ai response
    with st.spinner("Thinking..."):
        response = llm.invoke(prompt)
    with st.chat_message("ai"):
        st.write_stream(typewriter(response.text))
        
    # saving the message in chats
    st.session_state.chats.append({"role" : "ai", "content" : response.text})