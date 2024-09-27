import streamlit as st

# Inject custom CSS for the About Me page
st.markdown(
    """
    <style>
    .stApp {
        background-color: peachpuff;  /* Peach background color */
    }
    .about-me-section {
        margin-top: 50px;
        text-align: center;
        color: black;
    }
    .navigate-button {
        display: block;
        width: 200px;
        margin: 20px auto;
        padding: 10px;
        text-align: center;
        background-color: #007bff;
        color: white;
        border: none;
        border-radius: 5px;
        cursor: pointer;
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

# Button to go back to the main page
if st.button("Back to Main Page"):
    st.experimental_set_query_params(page=None)
    st.experimental_rerun()
