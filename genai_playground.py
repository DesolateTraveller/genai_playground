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
import PyMuPDF  # for extracting text from PDFs
#----------------------------------------
import openai
#
from langchain.chains import ConversationalRetrievalChain
from langchain.llms import OpenAI
from langchain.document_loaders import PyPDFLoader
from langchain.indexes import FAISS
from langchain.vectorstores import VectorstoreWrapper

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

openai.api_key = 'your_openai_api_key'

#---------------------------------------------------------------------------------------------------------------------------------
### Main Functions
#---------------------------------------------------------------------------------------------------------------------------------

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
    
    uploaded_files = st.file_uploader("Upload PDFs", type=["pdf"], accept_multiple_files=True)

    all_text = ""

    if uploaded_files:
        st.write("Uploaded files:")
        for uploaded_file in uploaded_files:
                st.write(f"- {uploaded_file.name}")

        pdf_reader = PyMuPDF.open(uploaded_file)
        for page_num in range(pdf_reader.page_count):
            page = pdf_reader.load_page(page_num)
            all_text += page.get_text()

    if not all_text:
        st.write("Please upload some PDF files to proceed.")

    if all_text:

        loader = PyPDFLoader([uploaded_file.name for uploaded_file in uploaded_files])
        documents = loader.load()
        index = FAISS.from_documents(documents, OpenAIEmbeddings())
        chain = ConversationalRetrievalChain(llm=OpenAI(), retriever=VectorstoreWrapper(index))

        query = st.text_input("Enter your question:")
        if query:
            response = chain.run(query)
            st.write("Answer:", response)

#-----------------------------------
### Webpage
#-----------------------------------

    if data_source == "Webpage" :

        st.subheader("Webpage | Q&A",divider='blue')
        st.caption("**:blue-background[This app allows you to chat with a webpage using local Llama-3 and RAG]**")       

        webpage_url = st.text_input("Enter Webpage URL", type="default")

        if webpage_url:
            loader = WebBaseLoader(webpage_url)
            docs = loader.load()
            text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=10)
            splits = text_splitter.split_documents(docs)

            embeddings = OllamaEmbeddings(model=llm_model)
            vectorstore = Chroma.from_documents(documents=splits, embedding=embeddings)

            @st.cache_data(ttl="2h")
            def ollama_llm(question, context):
                formatted_prompt = f"Question: {question}\n\nContext: {context}"
                response = ollama.chat(model=llm_model, 
                                       messages=[{'role': 'user', 'content': formatted_prompt}])
                return response['message']['content']
            
            retriever = vectorstore.as_retriever()

            @st.cache_data(ttl="2h")
            def combine_docs(docs):
                return "\n\n".join(doc.page_content for doc in docs)

            @st.cache_data(ttl="2h")
            def rag_chain(question):
                retrieved_docs = retriever.invoke(question)
                formatted_context = combine_docs(retrieved_docs)
                return ollama_llm(question, formatted_context)

            st.success(f"Loaded {webpage_url} successfully!")

        #-----------------------------------
                      
        col1, col2 = st.columns((0.3,0.7))

        with col1:

            st.subheader("Question",divider='blue')
            prompt = st.text_input("**:blue[Ask a question about the PDF]**")

            if prompt:
                with st.spinner("Generating answer..."):
                    with col2:

                        st.subheader("Answer",divider='blue')
                        st.success("**Answer generated successfully**")
                        answer = rag_chain(prompt)
                        st.write(answer)
