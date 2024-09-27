import streamlit as st
import base64
import time

# Inject custom CSS to change the background color and style the page
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
        flex-wrap: wrap;  /* Ensure icons wrap if needed */
    }
    .down-arrow-container {
        display: flex;
        justify-content: center;  /* Center the arrow horizontally */
        margin-top: 20px;  /* Space between icons and arrow */
    }
    .down-arrow {
        width: 40px;
        height: 40px;
        cursor: pointer;
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
twitter_png_base64 = load_image_as_base64("twitter.png")
down_arrow_png_base64 = load_image_as_base64("down_arrow.png")

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

# Display the icons with hyperlinks
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
        <a href="https://x.com/manojrajal">
            <img src="data:image/png;base64,{twitter_png_base64}" alt="Twitter Icon" style="width:40px;height:40px;">
        </a>
    </div>
    <div class="down-arrow-container">
        <a href="/about_me">
            <img src="data:image/png;base64,{down_arrow_png_base64}" alt="Down Arrow" class="down-arrow">
        </a>
    </div>
    """,
    unsafe_allow_html=True
)
