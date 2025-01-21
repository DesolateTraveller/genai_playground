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
                   page_icon='https://www.clariant.com/images/clariant-logo-small.svg',
                   layout="wide",
                   initial_sidebar_state="collapsed",)
#---------------------------------------
#st.title(f""":rainbow[MegaMax | Activity Guiding Tool]""")
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
        <p>© 2025 | Created by : <span class="highlight">Avijit Chakraborty</span> | Prepared by: <a href="mailto:avijit.mba18@gmail.com">Avijit Chakraborty</a></p> <span class="highlight">Thank you for visiting the app | Unauthorized uses or copying is strictly prohibited | For best view of the app, please zoom out the browser to 75%.</span>
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
