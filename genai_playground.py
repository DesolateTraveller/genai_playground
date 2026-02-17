#---------------------------------------------------------------------------------------------------------------------------------
### Authenticator
#---------------------------------------------------------------------------------------------------------------------------------
import streamlit as st
#from streamlit_navigation_bar import st_navbar
#---------------------------------------------------------------------------------------------------------------------------------
### Import Libraries
#---------------------------------------------------------------------------------------------------------------------------------

#----------------------------------------
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
#----------------------------------------
from PIL import Image
#---------------------------------------------------------------------------------------------------------------------------------
### Title and description for your Streamlit app
#---------------------------------------------------------------------------------------------------------------------------------
st.set_page_config(page_title="Digi-e | v0.1",
                   page_icon="💻",
                   layout="wide",
                   initial_sidebar_state="collapsed",)
#---------------------------------------
st.markdown(
    """
    <style>
    .title-large {
        text-align: center;
        font-size: 35px;
        font-weight: bold;
        background: linear-gradient(to left, red, orange, blue, indigo, violet);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .title-small {
        text-align: center;
        font-size: 20px;
        background: linear-gradient(to left, red, orange, blue, indigo, violet);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .version-badge {
        text-align: center;
        display: inline-block;
        background: linear-gradient(120deg, #0056b3, #0d4a96);
        color: white;
        padding: 2px 12px;
        border-radius: 20px;
        font-size: 1.15rem;
        margin-top: 8px;
        font-weight: 600;
        letter-spacing: 0.5px;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.15);
    }
    </style>
    <div style="text-align: center;">
        <div class="title-large">Digital | Analytical | Generative AI</div>
        <div class="version-badge"> v0.2 </div>
    </div>
    """,
    unsafe_allow_html=True
)
#----------------------------------------
st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #F0F2F6;
        text-align: center;
        padding: 10px;
        font-size: 14px;
        color: #333;
        z-index: 100;
    }
    .footer p {
        margin: 0;
    }
    .footer .highlight {
        font-weight: bold;
        color: blue;
    }
    </style>

    <div class="footer">
        <p>© 2026 | Created by : <span class="highlight">Avijit Chakraborty</span> <a href="mailto:avijit.mba18@gmail.com"> 📩 </a> | <span class="highlight">Thank you for visiting the app | Unauthorized uses or copying is strictly prohibited | For best view of the app, please zoom out the browser to 75%.</span> </p>
    </div>
    """,
    unsafe_allow_html=True)

#----------------------------------------
#st.divider()
#----------------------------------------

#---------------------------------------------------------------------------------------------------------------------------------
### CSS 
#---------------------------------------------------------------------------------------------------------------------------------
st.markdown("""
<style>
.clickable-card {
    background: white;
    border-radius: 16px;
    padding: 25px 20px;
    box-shadow: 0 6px 18px rgba(0, 30, 80, 0.09);
    transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    height: 100%;
    border: 1px solid rgba(0, 86, 179, 0.08);
    position: relative;
    overflow: hidden;
    cursor: pointer;
    text-align: center;
    text-decoration: none;
    color: inherit;
    display: block;
}
.clickable-card:hover {
    transform: translateY(-8px);
    box-shadow: 0 12px 28px rgba(0, 30, 80, 0.18);
    border-color: rgba(0, 86, 179, 0.25);
}
.clickable-card:hover::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 5px;
    background: linear-gradient(90deg, #0056b3, #4da6ff);
}
.clickable-card .card-icon {
    font-size: 3.2rem;
    margin-bottom: 15px;
    color: #0056b3;
    font-weight: bold;
}
.clickable-card .card-title {
    color: #004a96;
    font-size: 1.4rem;
    font-weight: 700;
    margin: 0 0 12px;
}
.clickable-card .card-desc {
    color: #4a5568;
    font-size: 0.95rem;
    line-height: 1.6;
    margin: 0;
    opacity: 0.9;
}
.card-link {
    text-decoration: none;
    color: inherit;
    display: block;
    height: 100%;
}
</style>
""", unsafe_allow_html=True)

#---------------------------------------------------------------------------------------------------------------------------------
### Functions & Definitions
#---------------------------------------------------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------------------------------------------
### Main app
#---------------------------------------------------------------------------------------------------------------------------------
import streamlit as st

# ===== MAIN HEADER =====
st.markdown("""
<style>
.banner {
    background: linear-gradient(135deg, #f0f7ff 0%, #e6f2ff 100%);
    border-radius: 12px;
    padding: 15px;
    margin: 25px 0;
    border: 1px solid rgba(0, 86, 179, 0.15);
    text-align: center;
    font-size: 1.15rem;
    color: #0056b3;
    font-weight: 600;
}
</style>

<div class="banner">
    Click the cards below to access different sections and explore the following features
</div>
""", unsafe_allow_html=True)

# ===== CLICKABLE CARDS IN SINGLE ROW =====
st.markdown("""
<style>
.clickable-card {
    background: white;
    border-radius: 16px;
    padding: 25px 20px;
    box-shadow: 0 6px 18px rgba(0, 30, 80, 0.09);
    transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    height: 100%;
    border: 1px solid rgba(0, 86, 179, 0.08);
    position: relative;
    overflow: hidden;
    cursor: pointer;
    text-align: center;
    text-decoration: none;
    color: inherit;
    display: block;
}
.clickable-card:hover {
    transform: translateY(-8px);
    box-shadow: 0 12px 28px rgba(0, 30, 80, 0.18);
    border-color: rgba(0, 86, 179, 0.25);
}
.clickable-card:hover::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 5px;
    background: linear-gradient(90deg, #0056b3, #4da6ff);
}
.clickable-card .card-icon {
    font-size: 3.2rem;
    margin-bottom: 15px;
    color: #0056b3;
    font-weight: bold;
}
.clickable-card .card-title {
    color: #004a96;
    font-size: 1.4rem;
    font-weight: 700;
    margin: 0 0 15px;
}
.clickable-card .card-desc {
    color: #4a5568;
    font-size: 0.95rem;
    line-height: 1.6;
    margin: 0;
    opacity: 0.9;
}
.card-list {
    list-style-type: none;
    padding: 0;
    margin: 0;
    text-align: left;
}
.card-list li {
    margin-bottom: 8px;
    padding-left: 20px;
    position: relative;
}
.card-list li:before {
    content: '✓';
    position: absolute;
    left: 0;
    color: #0056b3;
    font-weight: bold;
    font-size: 1.1rem;
}
.card-link {
    text-decoration: none;
    color: inherit;
    display: block;
    height: 100%;
}
</style>
""", unsafe_allow_html=True)

# Create 7 columns for cards in a single row
col1, col2, col3, col4, col5, col6, col7 = st.columns(7)

# Card 1: Statistics Playground
with col1:
    st.markdown("""
    <a href="https://stat-playground.streamlit.app/" target="_blank" class="card-link">
        <div class="clickable-card">
            <div class="card-icon">📊</div>
            <h3 class="card-title">Statistics Playground</h3>
            <ul class="card-list">
                <li>Comprehensive statistical analysis</li>
                <li>Data visualization tools</li>
                <li>Investigate relationships within datasets</li>
            </ul>
        </div>
    </a>
    """, unsafe_allow_html=True)

# Card 2: PDF Playground
with col2:
    st.markdown("""
    <a href="https://pdf-playground.streamlit.app/" target="_blank" class="card-link">
        <div class="clickable-card">
            <div class="card-icon">📘</div>
            <h3 class="card-title">PDF Playground</h3>
            <ul class="card-list">
                <li>Preview and extract PDF content</li>
                <li>Extract metadata from PDFs</li>
                <li>Add or remove passwords</li>
                <li>Modify, merge, convert PDFs</li>
                <li>Compress PDF files</li>
            </ul>
        </div>
    </a>
    """, unsafe_allow_html=True)

# Card 3: Image Playground
with col3:
    st.markdown("""
    <a href="https://image-playground.streamlit.app/" target="_blank" class="card-link">
        <div class="clickable-card">
            <div class="card-icon">🖼️</div>
            <h3 class="card-title">Image Playground</h3>
            <ul class="card-list">
                <li>Upload and crop images</li>
                <li>Remove background</li>
                <li>Mirror and rotate images</li>
                <li>Convert to grayscale or black & white</li>
                <li>Adjust brightness, saturation, contrast</li>
                <li>Modify sharpness</li>
            </ul>
        </div>
    </a>
    """, unsafe_allow_html=True)

# Card 4: ML Studio
with col4:
    st.markdown("""
    <a href="https://ml-studio.streamlit.app/" target="_blank" class="card-link">
        <div class="clickable-card">
            <div class="card-icon">📈</div>
            <h3 class="card-title">ML Studio</h3>
            <ul class="card-list">
                <li>Lightweight ML application</li>
                <li>Analyze different ML problems</li>
                <li>Machine learning model training</li>
                <li>Prediction and evaluation tools</li>
            </ul>
        </div>
    </a>
    """, unsafe_allow_html=True)

# Card 5: Web Scrapper
with col5:
    st.markdown("""
    <a href="https://web-scrapper.streamlit.app/" target="_blank" class="card-link">
        <div class="clickable-card">
            <div class="card-icon">🌐</div>
            <h3 class="card-title">Web Scrapper</h3>
            <ul class="card-list">
                <li>Extract information from webpages</li>
                <li>Upload multiple links</li>
                <li>Scrape structured data</li>
                <li>Export scraped data</li>
            </ul>
        </div>
    </a>
    """, unsafe_allow_html=True)

# Card 6: GenAI Studio
with col6:
    st.markdown("""
    <a href="#" target="_blank" class="card-link">
        <div class="clickable-card">
            <div class="card-icon">📝</div>
            <h3 class="card-title">GenAI Studio</h3>
            <ul class="card-list">
                <li>Text summarization</li>
                <li>Question & Answer systems</li>
                <li>Content generation</li>
                <li>Language translation</li>
                <li>Format conversion</li>
            </ul>
        </div>
    </a>
    """, unsafe_allow_html=True)

# Card 7: Chatbot
with col7:
    st.markdown("""
    <a href="#" target="_blank" class="card-link">
        <div class="clickable-card">
            <div class="card-icon">💬</div>
            <h3 class="card-title">Chatbot</h3>
            <ul class="card-list">
                <li>AI-powered chatbot</li>
                <li>Conversational interface</li>
                <li>Natural language processing</li>
                <li>Interactive responses</li>
            </ul>
        </div>
    </a>
    """, unsafe_allow_html=True)
