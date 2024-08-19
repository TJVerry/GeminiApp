# Gemini AI Apps - README #
### Overview ### 
This repository contains two Python applications built with Streamlit that leverage Google's Gemini generative AI models. Each app demonstrates a different use case of the Gemini model:

Gemini Text-based Model (gemini-1.5-flash): A simple conversational AI that takes user input as text and generates responses.
Gemini Multimodal Model (gemini-1.5-pro): An enhanced version that accepts both text and image inputs to generate responses based on the combination of both modalities.
These apps can be used for conversational AI, generating insights, or understanding text and image content.

### Features ### 
* App 1: Gemini AI - Text-based Model
- Model: gemini-1.5-flash
- Input: Text
- Output: AI-generated response based on the input text.
- Use Case: General Q&A, conversational AI.
* App 2: Gemini AI - Multimodal Model
- Model: gemini-1.5-pro
- Input: Text and Image
- Output: AI-generated response based on the provided text and image.
- Use Case: Text and image analysis, content generation, or understanding visual context combined with text.

### Prerequisites ### 
* Python 3.9+
* Streamlit
* Google Generative AI SDK
* dotenv (for environment variable management)
* PIL (Python Imaging Library)

### Setup Instructions ###
1. Clone this repository:

`git clone <repository-url>`
`cd gemini-ai-apps`

2. Install the required Python packages:

`pip install -r requirements.txt`

3. Set up your Google API key:
4. Create a .env file in the project root.
5. Add your Google API key to the .env file:

`GOOGLE_API_KEY= "{your-google-api-key-here}"`

6. Run the desired Streamlit app:
For the text-based app:

`streamlit run app.py`
For the multimodal app:

`streamlit run vision.py`

### License ###
This project is licensed under the MIT License. See the LICENSE file for details.

Contact
For any questions or issues, please open a GitHub issue or reach out to the repository maintainer.

