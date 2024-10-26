import streamlit as st

def chatbot_response(user_input):
    """Simple chatbot responses based on predefined questions."""
    responses = {
        "hi": "Hello! How can I assist you today?",
        "how are you": "I'm a chatbot, but thanks for asking! How can I help you?",
        "bye": "Goodbye! Have a great day!",
        "what's your name?": "I'm just a simple chatbot without a name, but you can call me Chatbot!",
        "tell me a joke": "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "what can you do?": "I can help summarize text or chat with you! Just let me know what you need.",
        "help": "I'm here to help! You can ask me about text summarization or just chat.",
        "thank you": "You're welcome! If you have more questions, feel free to ask.",
        "what time is it?": "I can't tell the time, but I hope you're having a great day!",
        "who created you?": "I was created by a programmer to assist users like you!",
        "where are you from?": "I'm from the digital world, here to help you anytime!",
        "what's your favorite color?": "I don't have preferences, but I think blue is a nice color!",
    }
    return responses.get(user_input.lower(), "I'm here to help! Tell me more.")

def display_chatbot():
    st.header("Simple Chatbot")
    
    # Initialize session state for chat history
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []

    # Display chat history
    for user_message, bot_message in st.session_state.chat_history:
        st.write(f"You: {user_message}")
        st.write(f"Chatbot: {bot_message}")

    # User input
    user_input = st.text_input("You:", "")
    
    if st.button("Send"):
        if user_input:
            # Get bot response
            bot_response = chatbot_response(user_input)
            st.write(f"You: {user_input}")  # Display user message
            st.write(f"Chatbot: {bot_response}")  # Display bot message
        else:
            st.warning("Please enter a message to start the chat.")
