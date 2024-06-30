import streamlit as st
import PyPDF2  # for extracting text from PDFs
import openai
from langchain.llms import OpenAI
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import ConversationalRetrievalChain

# Set your OpenAI API key
openai.api_key = 'your_openai_api_key'

# Streamlit app title
st.title("Ask Questions from Multiple PDFs")

# Upload PDFs
uploaded_files = st.file_uploader("Upload PDFs", type=["pdf"], accept_multiple_files=True)

# Initialize an empty string to store all texts from PDFs
all_text = ""

if uploaded_files:
    st.write("Uploaded files:")
    for uploaded_file in uploaded_files:
        st.write(f"- {uploaded_file.name}")

        # Extract text from each PDF using PyPDF2
        pdf_reader = PyPDF2.PdfReader(uploaded_file)
        
        # Extract text from each page
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
# If no PDFs are uploaded, prompt the user
if not all_text:
    st.write("Please upload some PDF files to proceed.")

# If PDFs are uploaded and text is extracted
if all_text:
    # Split the text into manageable chunks
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    documents = text_splitter.split_text(all_text)

    # Embed the chunks using OpenAI embeddings
    embeddings = OpenAIEmbeddings()
    index = FAISS.from_texts(documents, embeddings)

    # Initialize ConversationalRetrievalChain
    chain = ConversationalRetrievalChain.from_chain_type(
        llm=OpenAI(),
        chain_type="stuff",
        retriever=index.as_retriever()
    )

    # Get user query
    query = st.text_input("Enter your question:")

    if query:
        # Get the answer
        response = chain.run(query)

        # Display the answer
        st.write("Answer:", response)
