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
st.markdown("""
<style>
    /* Container for the link to remove default underline */
    .card-link {
        text-decoration: none;
        color: inherit;
        display: block;
        height: 100%;
    }

    /* The Card Itself - COMPACT SIZE */
    .clickable-card {
        background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
        border: 1px solid #eef2f6;
        border-top: 4px solid #4F8BF9;
        border-radius: 12px;
        padding: 15px 12px;  /* 👈 Reduced padding for smaller cards */
        height: 100%;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05);
        transition: all 0.3s ease;
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
        min-height: 300px;  /* 👈 Compact fixed height */
    }

    /* Hover Effect */
    .clickable-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 12px 25px rgba(79, 139, 249, 0.25);
        border-top-color: #2c5282;
    }

    /* Icon Styling - Slightly smaller for compact cards */
    .card-icon {
        font-size: 2rem;  /* 👈 Reduced from 3rem */
        margin-bottom: 10px;
        filter: drop-shadow(0 2px 4px rgba(0,0,0,0.1));
        line-height: 1;
    }
    /* Title - Comfortable & Readable */
    .card-title {
        font-size: 1.05rem;
        font-weight: 600;
        color: #1a5490;
        margin: 0 0 14px 0;
        line-height: 1.3;
    }

    /* Feature List - Eye-soothing */
    .card-list {
        list-style: none;
        padding: 0;
        margin: 0;
        width: 100%;
        text-align: left;
        flex-grow: 1;
    }

    .card-list li {
        font-size: 0.85rem;
        color: #5a6c7d;
        margin-bottom: 8px;
        padding-left: 20px;
        position: relative;
        line-height: 1.5;
        font-weight: 400;
    }

    /* Custom Checkmark Bullet */
    .card-list li::before {
        content: '✓';
        position: absolute;
        left: 0;
        color: #4F8BF9;
        font-weight: bold;
        font-size: 1rem;
    }
    
    /* Fix for Streamlit column gaps */
    .stColumn {
        display: flex;
    }
    
    /* Responsive: wrap cards on smaller screens */
    @media (max-width: 1200px) {
        .clickable-card {
            min-height: 240px;
        }
    }
    @media (max-width: 768px) {
        .clickable-card {
            min-height: auto;
            padding: 12px 10px;
        }
        .card-title {
            font-size: 1.15rem;
        }
        .card-list li {
            font-size: 1.05rem;
        }
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

#----------------------------------------

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
num_cols = 5# 👈 Adjust this value to change number of columns (e.g., 4, 5, 6)
cols = st.columns(num_cols)

# Distribute cards across columns
for idx, card in enumerate(cards_data):
    col_idx = idx % num_cols  # Cycle through columns
    with cols[col_idx]:
        # Handle placeholder cards differently
        if card.get("placeholder"):
            card_html = f"""
            <div class="clickable-card" style="opacity: 0.6; border-style: dashed; cursor: default;">
                <div class="card-icon">{card['icon']}</div>
                <h3 class="card-title">{card['title']}</h3>
                <ul class="card-list">
                    {''.join(f"<li>{feat}</li>" for feat in card['features'])}
                </ul>
            </div>
            """
            st.markdown(card_html, unsafe_allow_html=True)
        else:
            card_html = f"""
            <a href="{card['url'].strip()}" target="_blank" class="card-link">
                <div class="clickable-card">
                    <div class="card-icon">{card['icon']}</div>
                    <h3 class="card-title">{card['title']}</h3>
                    <ul class="card-list">
                        {''.join(f"<li>{feat}</li>" for feat in card['features'])}
                    </ul>
                </div>
            </a>
            """
            st.markdown(card_html, unsafe_allow_html=True)

st.write("")  # Spacer at bottom
