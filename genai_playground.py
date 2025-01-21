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
    <div class="title">Digital & Generative AI Playground</div>
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

col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
with col1:
    if st.button("🏠 **Home**",use_container_width=True):
        st.session_state.current_page = "Home"
with col2:
    if st.button("📈 **ML Studio**",use_container_width=True):
        st.session_state.current_page = "ml_studio" 
with col3:
    if st.button("📕 **PDF Playground**",use_container_width=True):
        st.session_state.current_page = "pdf_playground"
with col4:
    if st.button("🖼️ **Image Playground**",use_container_width=True):
        st.session_state.current_page = "image_playground"              
with col5:
    if st.button("🌐 **Web Scapper**",use_container_width=True):
        st.session_state.current_page = "web_scapper"
with col6:
    if st.button("📝 **Text Extracter**",use_container_width=True):
        st.session_state.current_page = "text_extracter"
with col7:
    if st.button("💬 **Chatbot**",use_container_width=True):
        st.session_state.current_page = "chatbot"
        
page = st.session_state.current_page 

#---------------------------------------------------------------------------------------------------------------------------------
if page == "Welcome":
    
    st.divider()

    st.markdown("""
        <div style="background-color: #E6F5FF; padding: 25px; border-radius: 15px; text-align: center; max-width: 100%; margin: 20px auto; box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);">
            <h5 style="color: #6495ED;">Welcome to the App</h5>
            <p style="color: #4B4B4B;">
                click the button above to access different sections and explore the following features
            </p>            
            <ul style="color: #4B4B4B; text-align: left; margin-left: 20px; display: inline-block;">
                <li><strong>Home:</strong> Understand the project overview and get started with the app.</li>
                <li><strong>Machine Learning (ML) Studio:</strong> .</li>
            </ul>
        </div>
        """,unsafe_allow_html=True,) 
    
#---------------------------------------------------------------------------------------------------------------------------------
if page == "Home" :  

    st.divider()

#---------------------------------------------------------------------------------------------------------------------------------
if page == "ml_studio":
    
    st.divider()

    st.markdown("""
        <div style="background-color: #E6F5FF; padding: 15px; border-radius: 15px; text-align: center; max-width: 100%; margin: 10px auto; box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);">
            <a href="https://ml-studio.streamlit.app/" target="_blank" style="color: #007ACC; font-weight: bold; font-size: 20px; text-decoration: none;">
                ML Studio
            </a>
            <p style="color: #333; font-size: 16px; margin-top: 0; margin-bottom: 10px;">
                (click the above link for more details)
            </p>
        </div>
        """, unsafe_allow_html=True)

#---------------------------------------------------------------------------------------------------------------------------------    
if page == "pdf_playground":
    
    st.divider()

    st.markdown("""
        <div style="background-color: #E6F5FF; padding: 15px; border-radius: 15px; text-align: center; max-width: 100%; margin: 10px auto; box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);">
            <a href="https://pdf_playground.streamlit.app/" target="_blank" style="color: #007ACC; font-weight: bold; font-size: 20px; text-decoration: none;">
                PDF Playground
            </a>
            <p style="color: #333; font-size: 16px; margin-top: 0; margin-bottom: 10px;">
                (click the above link for more details)
            </p>
        </div>
        """, unsafe_allow_html=True)

#--------------------------------------------------------------------------------------------------------------------------------- 
if page == "image_playground":
    
    st.divider()

    st.markdown("""
        <div style="background-color: #E6F5FF; padding: 15px; border-radius: 15px; text-align: center; max-width: 100%; margin: 10px auto; box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);">
            <a href="https://imageplayground.streamlit.app/" target="_blank" style="color: #007ACC; font-weight: bold; font-size: 20px; text-decoration: none;">
                Image Playground
            </a>
            <p style="color: #333; font-size: 16px; margin-top: 0; margin-bottom: 10px;">
                (click the above link for more details)
            </p>
        </div>
        """, unsafe_allow_html=True)

#--------------------------------------------------------------------------------------------------------------------------------- 

if page == "web_scapper":
    
    #st.divider()
    
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
    st.markdown('<div class="centered-info"><span style="margin-left: 10px;">This app helps user to extract the information from a webpage by uploading the links</span></div>',unsafe_allow_html=True,)
    
#---------------------------------------------------------------------------------------------------------------------------------    
if page == "text_extracter":
    
    st.divider()
    
#---------------------------------------------------------------------------------------------------------------------------------    
elif page == "chatbot":
    
    st.divider()
