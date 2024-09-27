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
        gap: 10px;  /* Adjust spacing between icons as needed */
        margin-top: 20px;  /* Adjust space from the text */
        position: fixed;
        bottom: 10px;
        left: 10px;
        z-index: 1000;
    }
    .icon {
        opacity: 0;  /* Start with icon hidden */
        transition: opacity 5s ease-in;  /* Adjust timing and easing for the fade-in effect */
    }
    .icon.show {
        opacity: 1;  /* Make icon fully visible */
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

# Add space before displaying the icons
st.markdown("<br>" * 7, unsafe_allow_html=True)  # Adds 7 line breaks

# Display both email and GitHub icons with hyperlinks after text has finished typing
st.markdown(
    f"""
    <div class="icons-container">
        <a href="mailto:rajalbandi.manoj@gmail.com" class="icon" id="email-icon">
            <img src="data:image/svg+xml;base64,{email_svg_base64}" alt="Email Icon" style="width:40px;height:40px;">
        </a>
        <a href="https://github.com/your-github-username" class="icon" id="github-icon">
            <img src="data:image/png;base64,{github_png_base64}" alt="GitHub Icon" style="width:40px;height:40px;">
        </a>
    </div>
    <script>
    setTimeout(function() {{
        document.getElementById('email-icon').classList.add('show');
        document.getElementById('github-icon').classList.add('show');
    }}, 3000);  // Adjust the delay in milliseconds (3000 ms = 3 seconds)
    </script>
    """,
    unsafe_allow_html=True
)
