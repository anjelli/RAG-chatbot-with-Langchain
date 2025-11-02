# Chatbot with RAG (Retrieval‐Augmented Generation) & LangChain

This project implements a **RAG chatbot** that answers user questions based on your provided documents. Instead of relying solely on a large language model’s built-in knowledge, the bot first retrieves relevant passages from your knowledge base and then generates responses grounded in that retrieved context.

## How It Works

### 1. Load  
Documents (e.g., PDFs) placed in the `data/` directory are loaded into the ingestion script.  
### 2. Split  
Large documents are broken into smaller chunks to fit context window and focus on relevant passages.  
### 3. Embed  
Each chunk is converted into a vector (embedding), representing its semantic meaning in a high-dimensional space.  
### 4. Store  
The embeddings are stored in a vector database (e.g., Chroma) for efficient similarity search.  
### 5. Retrieval & Generation  
When the user asks a question:  
- The question is embedded and compared against stored chunks to find the most relevant passages.  
- Those passages are passed—alongside the user’s query and conversation history—to the language model to generate a response grounded in the retrieved context.

## Why RAG?

Traditional chatbots relying solely on LLMs often generate generic or off-topic answers. RAG aligns the model’s output with **your own documents**, making responses more accurate and domain-specific.

## Installation

1. Clone the repo:  
   ```bash
   git clone https://github.com/ThomasJanssen-tech/Chatbot-with-RAG-and-LangChain.git
   cd Chatbot-with-RAG-and-LangChain

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


