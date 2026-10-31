import streamlit as st
import streamlit.components.v1 as components
import os
import requests
import json

# Set Streamlit Page Configuration
st.set_page_config(
    page_title="Zaythera WIPO TM Seach",
    page_icon="⚖️",
    layout="wide"
)

# Server-side Python Scraper function for WIPO Global Brand Database
def fetch_live_wipo_data(trademark, classes, country):
    url = "https://branddb.wipo.int/branddb/api/search/v1/"
    
    # Construct WIPO search query payload
    query_parts = [{"type": "text", "field": "BRAND", "value": trademark}]
    
    if classes and len(classes) > 0:
        query_parts.append({"type": "list", "field": "NICE_CLASS", "values": [str(c) for c in classes]})
    
    if country != "ALL":
        query_parts.append({"type": "text", "field": "ORIGIN", "value": country})

    payload = {
        "sort": "score desc",
        "start": 0,
        "rows": 20,
        "query": {
            "operator": "AND",
            "nested": query_parts
        }
    }
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    try:
        response = requests.post(url, json=payload, headers=headers, timeout=10)
        if response.status_code == 200:
            return response.json().get("docs", [])
    except Exception as e:
        print(f"WIPO Scrape Error: {e}")
    return []

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
