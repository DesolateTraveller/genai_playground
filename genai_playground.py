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
    unsafe_allow_html=True)
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
# Define the container style
st.markdown("""
<style>
.project-container {
    padding: 15px;
    font-size: 1.1rem;
    background-color: #effefe;
    border-radius: 15px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    margin-bottom: 15px;
    text-align: left;
    display: flex;
    flex-direction: column;
    height: 100%; /* Ensures equal height cards */
}
.project-container:hover {
    background-color: #E0CCD3;
    transform: translateY(-2px);
    transition: all 0.2s;
}
.card-link {
    text-decoration: none;
    font-weight: bold;
    color: #0073e6;
    font-size: 1.2em;
    margin-bottom: 10px;
    display: block;
}
.card-link:hover {
    color: #005bb5;
}
.card-title {
    margin: 5px 0;
    font-size: 1.1em;
    color: #333;
}
.card-list {
    list-style-type: none; /* Removes default bullets */
    padding: 0;
    margin-top: 10px;
    text-align: left;
    font-size: 1.1em;
    color: #555;
    flex-grow: 1; /* Pushes content to fill space */
}
.card-list li {
    margin-bottom: 6px;
    padding-left: 15px;
    position: relative;
}
.card-list li::before {
    content: "•";
    color: #0073e6;
    font-weight: bold;
    position: absolute;
    left: 0;
}
</style>
""", unsafe_allow_html=True)

#---------------------------------------------------------------------------------------------------------------------------------
### Functions & Definitions
#---------------------------------------------------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------------------------------------------
### Main app
#---------------------------------------------------------------------------------------------------------------------------------
st.markdown("""
<style>
.banner {
    background: linear-gradient(135deg, #f0f7ff 0%, #e6f2ff 100%);
    border-radius: 20px;
    padding: 15px;
    margin: 25px 0;
    border: 1px solid rgba(0, 86, 179, 0.15);
    text-align: center;
    font-size: 1.25rem;
    color: #0056b3;
    font-weight: 600;
}
</style>
<div class="banner">
    Click the cards below to access different sections and explore the following features
</div>
""", unsafe_allow_html=True)

cards_data = [
    {
        "title": "Statistics Playground",
        "icon": "📊",
        "url": "https://stat-playground.streamlit.app/",
        "features": [
            "Comprehensive statistical analysis",
            "Data visualization tools",
            "Investigate relationships within datasets",
            "Conduct statistical tests"
        ]
    },
    {
        "title": "PDF Playground",
        "icon": "📘",
        "url": "https://pdf-playground.streamlit.app/",
        "features": [
            "Preview and extract PDF content",
            "Extract metadata from PDFs",
            "Add or remove passwords",
            "Modify, merge, convert PDFs",
            "Compress PDF files"
        ]
    },
    {
        "title": "Image Playground",
        "icon": "🖼️",
        "url": "https://image-playground.streamlit.app/",
        "features": [
            "Upload and crop images",
            "Remove background",
            "Mirror and rotate images",
            "Convert to grayscale or B&W",
            "Adjust brightness & contrast",
            "Modify sharpness"
        ]
    },
    {
        "title": "Machine learning (ML) Studio",
        "icon": "📈",
        "url": "https://ml-studio.streamlit.app/",
        "features": [
            "Lightweight ML application",
            "Analyze different ML problems",
            "Machine learning model training",
            "Prediction and evaluation tools"
        ]
    },
    {
        "title": "Web Scrapper",
        "icon": "🌐",
        "url": "https://web-scrapper.streamlit.app/",
        "features": [
            "Extract information from webpages",
            "Upload multiple links",
            "Scrape structured data",
            "Export scraped data"
        ]
    },
    {
        "title": "GenAI Studio",
        "icon": "📝",
        "url": "#",  # 👈 Replace with actual URL
        "features": [
            "Text summarization",
            "Question & Answer systems",
            "Content generation",
            "Language translation",
            "Format conversion"
        ]
    },
    {
        "title": "Chatbot",
        "icon": "💬",
        "url": "#",  # 👈 Replace with actual URL
        "features": [
            "AI-powered chatbot",
            "Conversational interface",
            "Natural language processing",
            "Interactive responses"
        ]
    },
    {
        "title": "Forecasting Studio",
        "icon": "📈",
        "url": "https://ts-forecasting.streamlit.app/",  
        "features": [
            "Forecast new data",
            "Find trend based on historical data"
        ],
    },
    {
        "title": "ML Code Generator",
        "icon": "📈",
        "url": "https://ml-code-gen.streamlit.app//",  
        "features": [
            "Generate code based on request",
            "Options to develop full length code"
        ],
    },
    {
        "title": "Coming Soon",
        "icon": "➕",
        "url": None,
        "features": [
            "New tools arriving shortly",
            "Stay tuned for updates"
        ],
        "placeholder": True
    }    
]

#----------------------------------------
#num_cols = 5# 👈 Adjust this value to change number of columns (e.g., 4, 5, 6)
#cols = st.columns(num_cols)

# Create 4 columns
cols = st.columns(5)

# Render Cards
for i, card in enumerate(cards_data):
    with cols[i % 5]:
        # Handle URL logic (Disable link if None or #)
        if card['url'] and card['url'] != "#":
            link_tag = f'<a href="{card["url"].strip()}" target="_blank" class="card-link">{card["icon"]} {card["title"]}</a>'
        elif card.get("placeholder"):
            link_tag = f'<div class="card-title" style="color:#888;">{card["icon"]} {card["title"]}</div>'
        else:
            link_tag = f'<div class="card-title">{card["icon"]} {card["title"]} (Soon)</div>'

        # Generate List Items
        features_html = ''.join(f"<li>{feat}</li>" for feat in card['features'])

        st.markdown(
        f"""
        <div class="project-container">
            {link_tag}
            <ul class="card-list">
                {features_html}
            </ul>
        </div>
        """, unsafe_allow_html=True)
