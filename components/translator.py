import streamlit as st
from mtranslate import translate
import pandas as pd
import os
from gtts import gTTS
import base64

# Read language dataset
def load_languages():
    df = pd.read_csv('./data/language.csv')  # Adjust path as necessary
    df.dropna(inplace=True)
    return df['name'].to_list(), df['iso'].to_list()

# Create a dictionary of languages and their corresponding 2-letter language codes
def create_lang_dict(lang, langcode):
    return {lang[i]: langcode[i] for i in range(len(langcode))}

# Function to decode audio file for download
def get_binary_file_downloader_html(bin_file, file_label='File'):
    with open(bin_file, 'rb') as f:
        data = f.read()
    bin_str = base64.b64encode(data).decode()
    href = f'<a href="data:application/octet-stream;base64,{bin_str}" download="{os.path.basename(bin_file)}">Download {file_label}</a>'
    return href

# Function to handle translations and audio generation
def translate_and_generate_audio(inputtext, choice, lang_array):
    output = translate(inputtext, lang_array[choice])
    aud_file = gTTS(text=output, lang=lang_array[choice], slow=False)
    aud_file.save("lang.mp3")
    return output

# Function to display chat history
def display_chat_history():
    with st.expander("Chat History", expanded=True):
        for user_message, bot_message in st.session_state.chat_history:
            st.write(f"You: {user_message}")
            st.write(f"Translation: {bot_message}")

# Main application function
def display_language():
    lang, langcode = load_languages()
    lang_array = create_lang_dict(lang, langcode)

    # Initialize session state for chat history
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []

    # Layout
    st.title("Language-Translation")
    inputtext = st.text_area("Hi Please Enter text here to Translate", height=100)

    # Sidebar for selecting language
    choice = st.sidebar.radio('SELECT LANGUAGE', tuple(lang))

    c1, c2 = st.columns([4, 3])

    # Button for translation
    if st.button("Translate"):
        if len(inputtext) > 0:
            try:
                output = translate_and_generate_audio(inputtext, choice, lang_array)

                with c1:
                    st.text_area("TRANSLATED TEXT", output, height=200)

                # If speech support is available, render audio file
                with c2:
                    audio_file_read = open('lang.mp3', 'rb')
                    audio_bytes = audio_file_read.read()
                    st.audio(audio_bytes, format='audio/mp3')
                    st.markdown(get_binary_file_downloader_html("lang.mp3", 'Audio File'), unsafe_allow_html=True)

                # Save chat history
                st.session_state.chat_history.append((inputtext, output))
                display_chat_history()
            except Exception as e:
                st.error(e)
        else:
            st.warning("Please enter text to translate.")

if __name__ == "__main__":
    display_language()
