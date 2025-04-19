import os
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from dotenv import load_dotenv, find_dotenv
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import CSVLoader
from langchain_core.runnables import RunnablePassthrough
from langchain_community.embeddings import OllamaEmbeddings  # Você pode trocar para OpenAIEmbeddings se preferir.

# Carrega variáveis de ambiente
_ = load_dotenv(find_dotenv())

# Conectando ao modelo da Groq
model_local = ChatGroq(
    model="mixtral-8x7b-32768",  # Pode usar mixtral, llama3, etc.
    api_key=os.getenv("GROQ_API_KEY")
)

ollama_server_url = "http://192.168.1.5:11434"

@st.cache_data
def load_csv_data():
    loader = CSVLoader(file_path="knowledge_base.csv")
    embeddings = OllamaEmbeddings(base_url=ollama_server_url, model='nomic-embed-text')
    documents = loader.load()
    vectorstore = FAISS.from_documents(documents, embeddings)
    retriever = vectorstore.as_retriever()
    return retriever

retriever = load_csv_data()

st.title("Aria - Sistema Inteligente")

rag_template = """
Você é um atendente de uma empresa.
Seu trabalho é conversar com os clientes, consultando a base de 
conhecimentos da empresa, e dar uma resposta simples e precisa baseada no contexto.

Contexto: {context}

Pergunta do cliente: {question}
"""
prompt = ChatPromptTemplate.from_template(rag_template)
chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | model_local
)

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if user_input := st.chat_input("Você:"):
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    response_stream = chain.stream({"text": user_input})    
    full_response = ""
    
    response_container = st.chat_message("assistant")
    response_text = response_container.empty()
    
    for partial_response in response_stream:
        full_response += str(partial_response.content)
        response_text.markdown(full_response + "▌")

    st.session_state.messages.append({"role": "assistant", "content": full_response})
