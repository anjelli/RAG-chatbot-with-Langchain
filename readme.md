# Chatbot with RAG and LangChain 

This project implements a **Retrieval-Augmented Generation (RAG) chatbot** using **LangChain**, **ChromaDB**, and **Sentence-Transformers** for local embeddings.  
It allows you to upload PDF documents, build a vector database, and interact with the content using a conversational interface built on **Gradio**.

---

## Features
- Uses **ChromaDB** for persistent vector storage and retrieval.
- Splits documents into context-aware chunks for efficient retrieval.
- Provides a **Gradio UI** for seamless chat interactions.
- Fully offline and privacy-preserving (no external API calls).

---

## Installation

### 1. Clone the repository
### 2. Create a Virtual Environment
```bash
python -m venv venv
```
### 3. Activate the Virtual Environment
```bash
For windows: venv\Scripts\activate
For Mac/Linux: source venv/bin/activate
```
### 4. Install Dependencies
```bash
pip install -r requirements.txt
```
### 5. Add API Key
Rename .env.example to .env

Open the file and add your API key:

HUGGINGFACEHUB_API_TOKEN=your_huggingface_api_token_here
(You can generate a free token from Hugging Face)

### Data Source

All PDFs used by the chatbot must be placed inside the /data folder.
During execution, the script will:

Load all PDF files from the /data directory.

Extract text and split it into smaller chunks.

Store embeddings locally in the /vectorstore folder for efficient retrieval.

### Execution
```bash
python ingest_database.py
python chatbot.py
```

