from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-pro")

# Function to Load Gemini model and respond to user input
def generate_response(input_text, image):
    if input_text != "":
        response = model.generate_content([input_text, image])
    else:
        response = model.generate_content(image)
    return response.text

# Streamlit App
st.set_page_config(page_title="Gemini AI", page_icon="📸")
st.header("Gemini AI")
input_text = st.text_input("Enter your question here", key = "input_text")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

submit_button = st.button("What is this?")

# If submit button is clicked

if submit_button:
    response = generate_response(input_text, image)
    st.write(response)