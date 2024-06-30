#---------------------------------------------------------------------------------------------------------------------------------
### Authenticator
#---------------------------------------------------------------------------------------------------------------------------------
import streamlit as st
#---------------------------------------------------------------------------------------------------------------------------------
### Import Libraries
#---------------------------------------------------------------------------------------------------------------------------------
import io
import os
import json
import time
import base64
import tempfile
import requests
import warnings
from PIL import Image
from random import randint
from io import BytesIO
warnings.filterwarnings("ignore")
#----------------------------------------
#import cv2
import PyPDF2
#import fitz
import pdf2image
#import docx
import docx2txt
#from docx import Document
#from pptx import Presentation
import pytesseract
from pytesseract import Output, TesseractError
#----------------------------------------
import openai
#

#---------------------------------------------------------------------------------------------------------------------------------
### Title and description for your Streamlit app
#---------------------------------------------------------------------------------------------------------------------------------
#import custom_style()
st.set_page_config(page_title="Digi-e",
                   layout="wide",
                   #page_icon=               
                   initial_sidebar_state="collapsed")
#----------------------------------------
st.title(f""":rainbow[Digi-e | v0.1]""")
st.markdown('Created by | <a href="mailto:avijit.mba18@gmail.com">Avijit Chakraborty</a>', 
            unsafe_allow_html=True)
st.info('**Disclaimer : :blue[Thank you for visiting the app] | Unauthorized uses or copying of the app is strictly prohibited | Click the :blue[sidebar] to follow the instructions to start the applications.**', icon="ℹ️")
#----------------------------------------
# Set the background image
st.divider()

#---------------------------------------------------------------------------------------------------------------------------------
### LLM Hyperparameters
#---------------------------------------------------------------------------------------------------------------------------------

#stats_expander = st.sidebar.expander("**:blue[LLM HyperParameters]**", expanded=False)
#with stats_expander: 
with st.sidebar.popover("**:blue[LLM HyperParameters]**", help="Tune the hyperparameters whenever required"):  
    llm_model = st.selectbox("**Select LLM**", ["llama3:instruct","anthropic.claude-v2:1","amazon.titan-text-express-v1","ai21.j2-ultra-v1","anthropic.claude-3-sonnet-20240229-v1:0"])
    max_tokens = st.number_input("**Max Tokens**", value=250)
    temperature= st.number_input(label="**Temperature (randomness)**",step=.1,format="%.2f", value=0.7)
    top_p= st.number_input(label="**top_p (cumulative probability)**",step=.01,format="%.2f", value=0.9)
    top_k= st.number_input(label="**top_k (top k most probable tokens)**",step=10, value=250)                                  
    chunk_size= st.number_input(label="**chunk_size (managable segments)**",step=100, value=10000) 
    chunk_overlap= st.number_input(label="**chunk_overlap (overlap between chunks)**",step=100, value=1000) 

openai.api_key = 'sk-proj-xvqhdaixDa0QtfXJxzcOT3BlbkFJjn691lYWMU2A9In7192C'

#---------------------------------------------------------------------------------------------------------------------------------
### Main Functions
#---------------------------------------------------------------------------------------------------------------------------------

@st.cache_data(ttl="2h")
def extract_text_from_pdf(uploaded_file):
    try:
        # Open the PDF file
        pdf_reader = PyPDF2.PdfReader(uploaded_file)
        
        # Extract text from each page
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        
        return text
    except Exception as e:
        st.error(f"Error occurred while extracting text from PDF: {e}")
        return None
    
@st.cache_data(ttl="2h")
def extract_text_from_pdf_s3(pdf_bytes):
    pdf_file = BytesIO(pdf_bytes)
    text = ""
    with pdf_file as f:
        pdf_reader = PyPDF2.PdfReader(f)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

#---------------------------------------------------------------------------------------------------------------------------------
### Main App
#---------------------------------------------------------------------------------------------------------------------------------

st.sidebar.header("Input", divider='blue')
st.sidebar.info('Please choose from the following options and follow the instructions to start the application.', icon="ℹ️")
action_type = st.sidebar.radio("**:blue[Choose the action]**", ["Q&A", "Chatbot"])
st.sidebar.divider()

#-----------------------------------

if action_type == "Q&A" :
    
    data_source = st.sidebar.radio("**:blue[Select the file type]**", ["PDF","PPT","Word","Excel","Image","Video","Email","Webpage"])
    st.sidebar.divider() 

#-----------------------------------
### PDF
#-----------------------------------

if data_source == "PDF" :
    
    uploaded_file = st.file_uploader("Upload PDFs", type=["pdf"])
    st.sidebar.divider()

    if uploaded_file is not None:
        text = extract_text_from_pdf(uploaded_file)

    stats_expander = st.expander("**:blue[Information]**", expanded=True)
    with stats_expander:

        txt = st.text_area(":blue[Extracted output from uploaded file]", value=text, height=500)
        st.info(f'Total **:blue[{len(txt)} characters.]**')


#-----------------------------------
### Webpage
#-----------------------------------


