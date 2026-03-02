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

#---------------------------------------------------------------------------------------------------------------------------------
### CSS 
#---------------------------------------------------------------------------------------------------------------------------------
st.markdown("""
<style>
    /* Container for the link to remove default underline */
    .card-link {
        text-decoration: none;
        color: inherit;
        display: block;
        height: 100%;
    }

    /* The Card Itself */
    .clickable-card {
        background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%); /* Subtle bright gradient */
        border: 1px solid #eef2f6;
        border-top: 4px solid #4F8BF9; /* Bright Blue Accent Top Border */
        border-radius: 16px;
        padding: 25px;
        height: 100%; /* Force equal height within column */
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05); /* Soft shadow */
        transition: all 0.3s ease;
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
    }

    /* Hover Effect: Lift up and glow */
    .clickable-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 12px 25px rgba(79, 139, 249, 0.25); /* Blue glow on hover */
        border-top-color: #2c5282;
    }

    /* Icon Styling */
    .card-icon {
        font-size: 3rem;
        margin-bottom: 15px;
        filter: drop-shadow(0 2px 4px rgba(0,0,0,0.1));
    }

    /* Title Styling */
    .card-title {
        font-size: 1.4rem;
        font-weight: 700;
        color: #2d3748;
        margin: 0 0 15px 0;
        letter-spacing: -0.5px;
    }

    /* List Styling */
    .card-list {
        list-style: none;
        padding: 0;
        margin: 0;
        width: 100%;
        text-align: left;
        flex-grow: 1; /* Pushes content to fill height */
    }

    .card-list li {
        font-size: 0.95rem;
        color: #4a5568;
        margin-bottom: 10px;
        padding-left: 20px;
        position: relative;
        line-height: 1.5;
    }

    /* Custom Checkmark Bullet */
    .card-list li::before {
        content: '✓';
        position: absolute;
        left: 0;
        color: #4F8BF9;
        font-weight: bold;
    }
    
    /* Fix for Streamlit column gaps */
    .stColumn {
        display: flex;
    }
</style>
""", unsafe_allow_html=True)

#---------------------------------------------------------------------------------------------------------------------------------
### Functions & Definitions
#---------------------------------------------------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------------------------------------------
### Main app
#---------------------------------------------------------------------------------------------------------------------------------

#----------------------------------------
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




# --- 2. Layout: Two Rows of 4 Columns ---

# ROW 1
col1, col2, col3, col4 = st.columns(4)

# --- Card 1: Statistics Playground ---
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
                <li>Conduct statistical tests</li>
            </ul>
        </div>
    </a>
    """, unsafe_allow_html=True)

# --- Card 2: PDF Playground ---
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

# --- Card 3: Image Playground ---
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
                <li>Convert to grayscale or B&W</li>
                <li>Adjust brightness & contrast</li>
                <li>Modify sharpness</li>
            </ul>
        </div>
    </a>
    """, unsafe_allow_html=True)

# --- Card 4: ML Studio ---
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

st.write("") # Spacer

# ROW 2
col5, col6, col7, col8 = st.columns(4)

# --- Card 5: Web Scrapper ---
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

# --- Card 6: GenAI Studio ---
with col6:
    # Replace '#' with your actual GenAI URL
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

# --- Card 7: Chatbot ---
with col7:
    # Replace '#' with your actual Chatbot URL
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

# --- Card 8: Placeholder (Optional) ---
# If you only have 7 cards, this column will be empty. 
# You can add an 8th card here or leave it blank.
with col8:
    st.markdown("""
    <div class="clickable-card" style="opacity: 0.6; border-style: dashed;">
        <div class="card-icon">➕</div>
        <h3 class="card-title">Coming Soon</h3>
        <ul class="card-list">
            <li>New tools arriving shortly</li>
            <li>Stay tuned for updates</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
