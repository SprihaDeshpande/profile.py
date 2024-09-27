import streamlit as st

# Inject custom CSS for the About Me page
st.markdown(
    """
    <style>
    .stApp {
        background-color: lightgray;
    }
    .about-me-section {
        margin-top: 50px;
        text-align: center;
        color: black;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# About Me section
st.markdown(
    """
    <div class="about-me-section">
        <h1>About Me</h1>
        <p>Here is some information about me...</p>
    </div>
    """,
    unsafe_allow_html=True
)

