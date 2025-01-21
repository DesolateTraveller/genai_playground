#---------------------------------------------------------------------------------------------------------------------------------
### Authenticator
#---------------------------------------------------------------------------------------------------------------------------------
import streamlit as st
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
    .title {
        text-align: center;
        font-size: 40px;
        font-weight: bold;
        background: linear-gradient(to left, red, orange, blue, indigo, violet);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    </style>
    <div class="title">Digi-e | Digital & Generative AI Playground</div>
    """,
    unsafe_allow_html=True
)
#----------------------------------------

st.markdown("""
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #F9F9FB;
        text-align: center;
        padding: 5px;
        font-size: 15px;
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
        <p>© 2025 | Created by : <span class="highlight">Avijit Chakraborty</span> | <a href="mailto:avijit.mba18@gmail.com"> 📩 </a></p> <span class="highlight">Thank you for visiting the app | Unauthorized uses or copying is strictly prohibited | For best view of the app, please zoom out the browser to 75%.</span>
    </div>
    """,
    unsafe_allow_html=True)

#----------------------------------------
#st.divider()
#----------------------------------------

#---------------------------------------------------------------------------------------------------------------------------------
### knowledge 
#---------------------------------------------------------------------------------------------------------------------------------


#---------------------------------------------------------------------------------------------------------------------------------
### Functions & Definitions
#---------------------------------------------------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------------------------------------------
### Main app
#---------------------------------------------------------------------------------------------------------------------------------

if "current_page" not in st.session_state:
    st.session_state.current_page = "Welcome"

#st.sidebar.subheader("**:blue[Contents]**",divider='blue')

col1, col2, col3, col4 = st.columns(4)
with col1:
    if st.button("🏠 **Home**",use_container_width=True):
        st.session_state.current_page = "Home"
with col2:
    if st.button("🌐 **Web Scapper**",use_container_width=True):
        st.session_state.current_page = "web_scapper"
with col3:
    if st.button("📝 **Text Extracter**",use_container_width=True):
        st.session_state.current_page = "text_extracter"
with col4:
    if st.button("💬 **Chatbot**",use_container_width=True):
        st.session_state.current_page = "chatbot"
        
page = st.session_state.current_page 

#---------------------------------------------------------------------------------------------------------------------------------
if page == "Welcome":
    
    st.divider()

    st.markdown("""
        <div style="background-color: #F0F8FF; padding: 20px; border-radius: 10px; text-align: center; max-width: 800px; margin: 0 auto;">
            <h5 style="color: #6495ED;">Welcome to the App</h5>
            <p style="color: #4B4B4B;">
                click the button above to access different sections and explore the following features
            </p>
            <ul style="color: #4B4B4B; text-align: left; margin-left: 20px; display: inline-block;">
                <li><strong>Home:</strong> Understand the project overview and get started with the app.</li>
                <li><strong>Analysis:</strong> Upload your data and explore step-by-step analytical tools.</li>
            </ul>
        </div>
        """,unsafe_allow_html=True,) 
    
#---------------------------------------------------------------------------------------------------------------------------------
if page == "Home" :  

    st.divider()

#---------------------------------------------------------------------------------------------------------------------------------    
if page == "web_scapper":
    
    st.divider()
    
    st.markdown(
            """
            <style>
                .centered-info {
                display: flex;
                justify-content: center;
                align-items: center;
                font-weight: bold;
                font-size: 15px;
                color: #007BFF; 
                padding: 5px;
                background-color: #E8F4FF; 
                border-radius: 5px;
                border: 1px solid #007BFF;
                margin-top: 5px;
                }
            </style>
            """,unsafe_allow_html=True,)
    st.markdown('<div class="centered-info"><span style="margin-left: 10px;">Inputs</span></div>',unsafe_allow_html=True,)
    
#---------------------------------------------------------------------------------------------------------------------------------    
if page == "text_extracter":
    
    st.divider()
    
#---------------------------------------------------------------------------------------------------------------------------------    
elif page == "chatbot":
    
    st.divider()
