import streamlit as st
from textblob import TextBlob

st.title("AI Sentiment Analyzer")

user_text = st.text_area("Enter your text")

if st.button("Analyze"):
    
    sentiment = TextBlob(user_text)
    
    if sentiment.sentiment.polarity > 0:
        st.success("Positive 😊")
        
    elif sentiment.sentiment.polarity < 0:
        st.error("Negative 😔")
        
    else:
        st.warning("Neutral 😐")