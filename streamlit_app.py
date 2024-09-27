import streamlit as st
import time

# Inject custom CSS to change the background color
st.markdown(
    """
    <style>
    .stApp {
        background-color: lightgray;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Create a container for the typing effect
container = st.empty()

# Text to be typed
text = "Hi, I am Manoj Rajalbandi, Software Engineer, Distributed Systems"

# Typing speed (seconds)
typing_speed = 0.05

# Initialize empty string
typed_text = ""

# Simulate typing effect
for char in text:
    typed_text += char
    container.markdown(f"# {typed_text}")  # Using Markdown header for large text
    time.sleep(typing_speed)

# Keep the final text displayed
container.markdown(f"# {text}")  # Markdown header with a single #
