import streamlit as st
import time
import base64

# Inject custom CSS to change the background color
st.markdown(
    """
    <style>
    .stApp {
        background-color: lightgray;
    }
    .icons-container {
        display: flex;
        justify-content: center;  /* Center icons horizontally */
        gap: 10px;  /* Adjust spacing between icons as needed */
        margin-top: 20px;  /* Adjust space from the text */
        margin-bottom: 20px;  /* Optional: Add space below the icons */
        z-index: 1000;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Function to load image files as base64
def load_image_as_base64(image_file_path):
    with open(image_file_path, "rb") as file:
        image_bytes = file.read()
    return base64.b64encode(image_bytes).decode()

# Load the images as base64
email_svg_base64 = load_image_as_base64("email.svg")
github_png_base64 = load_image_as_base64("github.png")
linkedin_png_base64 = load_image_as_base64("linkedin.png")
facebook_png_base64 = load_image_as_base64("facebook.png")

# Create a container for the typing effect
container = st.empty()

# Text to be typed
text = "Hi, I am Manoj Rajalbandi, a System Software Engineer - Distributed Systems"

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

# Add space before displaying the icons
st.markdown("<br>" * 7, unsafe_allow_html=True)  # Adds 7 line breaks

# Display the email, GitHub, LinkedIn, and Facebook icons with hyperlinks centered
st.markdown(
    f"""
    <div class="icons-container">
        <a href="mailto:rajalbandi.manoj@gmail.com">
            <img src="data:image/svg+xml;base64,{email_svg_base64}" alt="Email Icon" style="width:40px;height:40px;">
        </a>
        <a href="https://github.com/manojraj185">
            <img src="data:image/png;base64,{github_png_base64}" alt="GitHub Icon" style="width:40px;height:40px;">
        </a>
        <a href="https://www.linkedin.com/in/manoj-rajalbandi/">
            <img src="data:image/png;base64,{linkedin_png_base64}" alt="LinkedIn Icon" style="width:40px;height:40px;">
        </a>
        <a href="https://www.facebook.com/manoj.rajalbandi/">
            <img src="data:image/png;base64,{facebook_png_base64}" alt="Facebook Icon" style="width:40px;height:40px;">
        </a>
    </div>
    """,
    unsafe_allow_html=True
)
