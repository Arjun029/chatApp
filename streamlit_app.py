import streamlit as st
import base64
from components.text_summarizer import display_text_summarizer
from components.chatbot import display_chatbot
from components.translator import display_language

# Function to read and encode the image file
def get_base64_image(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    return encoded_string

# Function to apply background image using CSS
def set_background(option):
    background_images = {
        "Text Summarization": "images/summary.jpg",
        "Chatbot": "images/chatbot.jpg",
        "Transalator":"images/1.jpg"
    }
    
    image_path = background_images.get(option)
    if image_path:
        base64_image = get_base64_image(image_path)
        css = f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{base64_image}");
            background-size: cover;
            background-position: center;
        }}
        </style>
        """
        st.markdown(css, unsafe_allow_html=True)

st.title("Multi-Project Streamlit App")

option = st.selectbox("Choose a project:", ("Text Summarization", "Chatbot", "Transalator"))

set_background(option)

if option == "Text Summarization":
    display_text_summarizer()
elif option == "Chatbot":
    display_chatbot()
elif option == "Transalator":
    display_language()
