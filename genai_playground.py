import streamlit as st
import PyMuPDF  # for extracting text from PDFs
import openai
from langchain.chains import ConversationalRetrievalChain
from langchain.llms import OpenAI
from langchain.document_loaders import PyPDFLoader
from langchain.indexes import FAISS
from langchain.vectorstores import VectorstoreWrapper

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

        # Extract text from each PDF
        pdf_reader = PyMuPDF.open(uploaded_file)
        for page_num in range(pdf_reader.page_count):
            page = pdf_reader.load_page(page_num)
            all_text += page.get_text()

# If no PDFs are uploaded, prompt the user
if not all_text:
    st.write("Please upload some PDF files to proceed.")

# If PDFs are uploaded and text is extracted
if all_text:
    # Embed the extracted text using FAISS and LangChain
    loader = PyPDFLoader([uploaded_file.name for uploaded_file in uploaded_files])
    documents = loader.load()
    index = FAISS.from_documents(documents, OpenAIEmbeddings())

    # Initialize ConversationalRetrievalChain
    chain = ConversationalRetrievalChain(llm=OpenAI(), retriever=VectorstoreWrapper(index))

    # Get user query
    query = st.text_input("Enter your question:")

    if query:
        # Get the answer
        response = chain.run(query)

        # Display the answer
        st.write("Answer:", response)
