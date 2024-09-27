import streamlit as st
import time

# Create a container for the typing effect
container = st.empty()

# Text to be typed
text = "Hi, I am Manoj Rajalbandi, a Principal Software Engineer"

# Typing speed (seconds)
typing_speed = 0.05

# Initialize empty string
typed_text = ""

# Simulate typing effect
for char in text:
    typed_text += char
    container.markdown(f"<h1>{typed_text}</h1>", unsafe_allow_html=True)
    time.sleep(typing_speed)

# Keep the final text displayed
container.markdown(f"<h1>{text}</h1>", unsafe_allow_html=True)
