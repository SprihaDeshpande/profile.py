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
    .email-icon {
        opacity: 0;  /* Start with icon hidden */
        transition: opacity 5s ease-in;  /* Adjust timing and easing for the fade-in effect */
    }
    .email-icon.show {
        opacity: 1;  /* Make icon fully visible */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Load the SVG file as a base64-encoded string
def load_svg_as_base64(svg_file_path):
    with open(svg_file_path, "rb") as file:
        svg_bytes = file.read()
    return base64.b64encode(svg_bytes).decode()

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

# Load the email.svg as base64
svg_base64 = load_svg_as_base64("email.svg")

# Add space before displaying the email icon
st.markdown("<br>" * 7, unsafe_allow_html=True)  # Adds 7 line breaks

# Display the email icon as a hyperlink with a fade-in effect
st.markdown(
    f"""
    <div class="email-icon" id="email-icon">
        <a href="mailto:rajalbandi.manoj@gmail.com">
            <img src="data:image/svg+xml;base64,{svg_base64}" alt="Email Icon" style="width:40px;height:40px;">
        </a>
    </div>
    <script>
    setTimeout(function() {{
        document.getElementById('email-icon').classList.add('show');
    }}, 3000);  // Adjust the delay in milliseconds (3000 ms = 3 seconds)
    </script>
    """,
    unsafe_allow_html=True
)
