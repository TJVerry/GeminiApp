from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")

# Function to Load Gemini model and respond to user input
def generate_response(input_text):
    response = model.generate_content(input_text)
    return response.text

# Streamlit App
st.set_page_config(page_title="Gemini AI", page_icon="🔮")
st.header("Gemini AI")
input_text = st.text_input("Enter your question here", key = "input_text")

submit_button = st.button("Submit")

# When submit button is clicked
if submit_button:
    response = generate_response(input_text)
    st.write(response)