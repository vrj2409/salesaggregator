import streamlit as st
import streamlit.components.v1 as components
import os

# Set page config
st.set_page_config(
    page_title="Sales Intelligence Dashboard",
    page_icon="📊",
    layout="wide"
)

# Read the built HTML file
html_file_path = os.path.join('dist', 'index.html')

if os.path.exists(html_file_path):
    with open(html_file_path, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    # Inject the HTML into Streamlit
    components.html(html_content, height=1000, scrolling=True)
else:
    st.error("Dashboard files not found. Please ensure the dist folder is present.")
