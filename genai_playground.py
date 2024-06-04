#---------------------------------------------------------------------------------------------------------------------------------
### Authenticator
#---------------------------------------------------------------------------------------------------------------------------------
import streamlit as st
#---------------------------------------------------------------------------------------------------------------------------------
### Import Libraries
#---------------------------------------------------------------------------------------------------------------------------------
import os
import tempfile
#----------------------------------------
from embedchain import App

#---------------------------------------------------------------------------------------------------------------------------------
### Title and description for your Streamlit app
#---------------------------------------------------------------------------------------------------------------------------------
#import custom_style()
st.set_page_config(page_title="GenAI | Playground",
                   layout="wide",
                   #page_icon=               
                   initial_sidebar_state="collapsed")
#----------------------------------------
st.title(f""":rainbow[Generative AI | Playground | v0.1]""")
st.markdown('Created by | <a href="mailto:avijit.mba18@gmail.com">Avijit Chakraborty</a>', 
            unsafe_allow_html=True)
st.caption("This app allows you to chat with a PDF using Llama3 running locally wiht Ollama!")
st.info('**Disclaimer : :blue[Thank you for visiting the app] | Unauthorized uses or copying of the app is strictly prohibited | Click the :blue[sidebar] to follow the instructions to start the applications.**', icon="ℹ️")
#----------------------------------------
# Set the background image
st.divider()
#---------------------------------------------------------------------------------------------------------------------------------
### LLM Hyperparameters
#---------------------------------------------------------------------------------------------------------------------------------

stats_expander = st.sidebar.expander("**:blue[LLM HyperParameters]**", expanded=False)
with stats_expander: 
    llm_model = st.selectbox("**Select LLM**", ["llama3:instruct","anthropic.claude-v2:1","amazon.titan-text-express-v1","ai21.j2-ultra-v1","anthropic.claude-3-sonnet-20240229-v1:0"])
    max_tokens = st.number_input("**Max Tokens**", value=250)
    temperature= st.number_input(label="**Temperature (randomness)**",step=.1,format="%.2f", value=0.7)
    top_p= st.number_input(label="**top_p (cumulative probability)**",step=.01,format="%.2f", value=0.9)
    top_k= st.number_input(label="**top_k (top k most probable tokens)**",step=10, value=250)                                  
    chunk_size= st.number_input(label="**chunk_size (managable segments)**",step=100, value=10000) 
    chunk_overlap= st.number_input(label="**chunk_overlap (overlap between chunks)**",step=100, value=1000) 

#---------------------------------------------------------------------------------------------------------------------------------
### Main Functions
#---------------------------------------------------------------------------------------------------------------------------------
def embedchain_bot(db_path):
    return App.from_config(
        config={
            "llm": {"provider": "ollama", 
                    "config": {"model": llm_model, 
                               "max_tokens": max_tokens, 
                               "temperature": temperature, 
                               "stream": True, 
                               "base_url": 'http://localhost:11434'}},
            "vectordb": {"provider": "chroma", 
                         "config": {"dir": db_path}},
            "embedder": {"provider": "ollama", 
                         "config": {"model": llm_model, 
                                    "base_url": 'http://localhost:11434'}},
        }
    )

