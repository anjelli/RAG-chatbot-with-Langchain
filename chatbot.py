from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.llms import HuggingFaceHub
import gradio as gr
from dotenv import load_dotenv

load_dotenv()

DATA_PATH = r"data"
CHROMA_PATH = r"chroma_db"

embeddings_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# free text generation model
llm = HuggingFaceHub(
    repo_id="google/flan-t5-base",
    model_kwargs={"temperature": 0.5, "max_length": 512}
)

vector_store = Chroma(
    collection_name="example_collection",
    embedding_function=embeddings_model,
    persist_directory=CHROMA_PATH,
)

retriever = vector_store.as_retriever(search_kwargs={'k': 5})


def stream_response(message, history):
    docs = retriever.invoke(message)
    knowledge = "".join(doc.page_content + "\n\n" for doc in docs)

    rag_prompt = f"""
    Answer based only on the text below.
    Question: {message}
    Knowledge: {knowledge}
    """

    response = llm.invoke(rag_prompt)
    yield response


chatbot = gr.ChatInterface(
    stream_response,
    textbox=gr.Textbox(placeholder="Ask something...", container=False, autoscroll=True, scale=7),
)

chatbot.launch()
