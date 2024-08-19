from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-pro")
chat = model.start_chat(history=[])

def generate_response(query):
    response = chat.send_message(query, stream=True)
    return response
st.set_page_config(page_title="Gemini AI", page_icon="💬")
st.header("Gemini AI Chat App")

if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

input_text = st.text_input("Enter your question here", key = "input_text")
submit_button = st.button("Send")

if submit_button and input_text:
    response = generate_response(input_text)
    # Append the response to the chat history
    st.session_state['chat_history'].append(("You",input_text))

    # Show the response as it is streaming
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("AI",chunk.text))

st.subheader("Chat History")
for sender, message in st.session_state['chat_history']:
    st.write(f"{sender}: {message}")