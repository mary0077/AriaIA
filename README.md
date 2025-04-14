# 🤖 Aria - Inteligência Artificial

**Aria** é um sistema de atendimento inteligente desenvolvido com [Streamlit](https://streamlit.io/) e [LangChain](https://www.langchain.com/), capaz de responder perguntas de clientes com base em uma base de conhecimento interna. Ele utiliza modelos LLMs hospedados localmente e APIs da Groq, combinando tecnologias de *retrieval augmented generation* (RAG) para fornecer respostas precisas e contextualizadas.

---

## 🚀 Funcionalidades

- Interface web interativa com Streamlit.
- Processamento de linguagem natural com modelos LLM.
- Busca semântica com embeddings (nomic-embed-text via Ollama).
- Carregamento e consulta de base de conhecimento em CSV.
- Integração com Groq para geração de respostas.

---

## 🧱 Tecnologias Utilizadas

- **Python**
- **Streamlit**
- **LangChain**
- **Groq API**
- **FAISS** (para armazenamento vetorial)
- **Ollama Embeddings** (`nomic-embed-text`)
- **dotenv** (para carregar variáveis de ambiente)

---

## 📁 Estrutura esperada

project/ │ ├── knowledge_base.csv # Base de conhecimento em CSV ├── app.py # Código principal (o que está neste repositório) ├── .env # Arquivo com suas variáveis de ambiente (como GROQ_API_KEY) └── README.md # Este arquivo

---

## ⚙️ Variáveis de Ambiente

Crie um arquivo `.env` com o seguinte conteúdo:

GROQ_API_KEY=your_groq_api_key
