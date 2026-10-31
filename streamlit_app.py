import streamlit as st
import streamlit.components.v1 as components
import os

# Set Streamlit Page Configuration
st.set_page_config(
    page_title="IP-LexGuard Trademark Search",
    page_icon="⚖️",
    layout="wide"
)

# Hide default Streamlit padding for clean full-bleed UI
st.markdown("""
    <style>
        .block-container {
            padding-top: 1rem;
            padding-bottom: 0rem;
            padding-left: 1rem;
            padding-right: 1rem;
        }
        iframe {
            width: 100%;
            border: none;
        }
    </style>
""", unsafe_allow_html=True)

# Locate index.html in the current repository root directory
file_path = os.path.join(os.path.dirname(__file__), "index.html")

if os.path.exists(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        html_content = f.read()
    # Embed the full modern HTML app with scrolling enabled
    components.html(html_content, height=950, scrolling=True)
else:
    st.error("⚠️ `index.html` was not found in the root directory. Please commit both `streamlit_app.py` and `index.html` to your GitHub repository.")
