# Multi-Project Streamlit Application

This repository hosts a Streamlit application that offers three main functionalities: **Chatbot**, **Text Summarization**, and **Translator**. The app utilizes separate components to handle each feature, enabling users to interact with natural language processing tasks directly in their browser.

Link: [![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://arjunpotti.streamlit.app/)

## Features

### 1. Chatbot
The chatbot module is a conversational agent that responds to user inputs in real-time. It's designed to facilitate natural interactions, mimicking a chat experience with responses generated through NLP techniques.

### 2. Text Summarization
This module allows users to enter lengthy text, which is then summarized automatically. It provides concise summaries, helping users grasp the main points of any large text input quickly.

### 3. Translator
The translator module takes user-provided text and converts it to the selected language. It supports multiple languages, making it easy to translate text for various purposes. Additionally, the module generates an audio output of the translated text.

## Project Structure

The main Streamlit application is organized as follows:
```plaintext
.
├── streamlit_app.py           # Main Streamlit application file
├── components/
│   ├── chatbot.py             # Chatbot functionality module
│   ├── text_summarizer.py     # Text Summarization functionality module
│   └── translator.py          # Translator functionality module
├── data/
│   └── language.csv           # CSV file containing language codes for translation
├── images/
│   ├── summary.jpg            # Background image for Text Summarization module
│   ├── chatbot.jpg            # Background image for Chatbot module
│   └── translator.jpg         # Background image for Translator module
└── README.md                  # Project README file
```

## Requirements

Ensure you have the following libraries installed before running the application:
```plaintext
streamlit
pandas
spacy
langdetect
transformers
torch
en_core_web_sm
mtranslate
gtts
```

To install these dependencies, you can use the following command:
```bash
pip install -r requirements.txt
```

## Usage

### Running the App

1. **Navigate to the project directory**:
   ```bash
   cd /path/to/project
   ```

2. **Launch Streamlit**:
   ```bash
   streamlit run streamlit_app.py
   ```

3. **Choose a Functionality**:
   - **Chatbot**: Engage with a chatbot.
   - **Text Summarization**: Summarize large text inputs.
   - **Translator**: Translate text into a chosen language and download an audio file of the translation.

### App Interface

- **Dropdown Selector**: Choose between Chatbot, Text Summarization, and Translator.
- **Text Input Area**: Enter text for summarization or translation.
- **Audio Download**: Available for translated text in the Translator module.

## Customization

### Background Images
Each module has a customizable background image. You can replace the images in the `/images` directory with any background images of your choice.

## Troubleshooting

- **File Not Found Error**: Ensure that the images are correctly named and located in the `/images` directory.
- **Dependencies Issue**: Confirm that all packages in `requirements.txt` are installed.

## Contributing

Contributions to this repository are welcome. Feel free to submit a pull request with improvements or additional features.