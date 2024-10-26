# components/text_summarizer.py

import streamlit as st
import spacy
from heapq import nlargest

def calculate_sentence_scores(sentences, word_frequency):
    sentence_scores = {}

    for sentence in sentences:
        score = 0
        for token in sentence:
            word = token.text.lower()
            if word in word_frequency:
                score += word_frequency[word]
        
        sentence_scores[sentence.text] = score
    
    return sentence_scores


def simple_summarize(text):
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(text)

    filtered_tokens = [token.text for token in doc if not token.is_stop and not token.is_punct]

    word_frequency = {}
    for word in filtered_tokens:
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1
    
    max_word = max(word_frequency.values())
    for word in word_frequency.keys():
        word_frequency[word] = word_frequency[word]/max_word
    
    sentence_tokens = [sent for sent in doc.sents ]
    sentence_score = calculate_sentence_scores(sentence_tokens, word_frequency)
    
    length_paragraph = int(len(sentence_tokens)* 0.4)
    summary = nlargest(length_paragraph,sentence_score,key=sentence_score.get)
    return summary[0]


def display_text_summarizer():
    st.header("Text Summarization")
    input_text = st.text_area("Enter text to summarize", height=200)

    if st.button("Summarize"):
        text_to_summarize = input_text
        if input_text:
            summary = simple_summarize(text_to_summarize)
            st.write("**Summary:**", summary)
        else:
            st.warning("Please enter text to summarize.")
        