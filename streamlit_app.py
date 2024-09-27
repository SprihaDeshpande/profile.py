import streamlit as st
import time
from PIL import Image  # For loading the SVG image

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

# Load the SVG image
email_icon = Image.open("email.svg")

# Display the email icon as a hyperlink
st.markdown(
    """
    <a href="mailto:rajalbandi.manoj@gmail.com">
        <img src="data:image/svg+xml;base64,{encoded}" alt="Email Icon" style="width:40px;height:40px;">
    </a>
    """.format(encoded=st.image(email_icon, use_column_width=False)),
    unsafe_allow_html=True
)

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
    container.markdown(f"# {typed_text}")  # Using Markdown header for large text
    time.sleep(typing_speed)

# Keep the final text displayed
container.markdown(f"# {text}")  # Markdown header with a single #
