# Import Streamlit library
import streamlit as st

# Title
st.title("Typing Effect")

# Typing effect using HTML and CSS
st.markdown("""
<style>
  .typing {
    font-size: 48px;
    font-weight: bold;
    animation: type 2s steps(40);
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    text-align: center;
  }
  @keyframes type {
    from {
      width: 0;
    }
  }
</style>
<div class="typing">Hi, I am Manoj, a software engineer</div>
""", unsafe_allow_html=True)
