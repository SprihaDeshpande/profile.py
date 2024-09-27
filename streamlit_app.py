import streamlit as st
import time

# Create a container for the typing effect
container = st.empty()

# Text to be typed
text = "Hi, I am Manoj, a software engineer"

# Typing speed (seconds)
typing_speed = 0.05

# Initialize empty string
typed_text = ""

# Simulate typing effect
for char in text:
    typed_text += char
    container.write(typed_text)
    time.sleep(typing_speed)

# Keep the final text displayed
container.write(text)
