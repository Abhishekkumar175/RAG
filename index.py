from dotenv import load_dotenv

from pathlib import Path 
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_qdrant import QdrantVectorStore

load_dotenv() # Load environment variables from .env file


pdf_path=Path(__file__).parent / "JD_Cognizant Ace Team program.pdf"

#load this file in python program
loader = PyPDFLoader(file_path=pdf_path)
docs=loader.load()

# Split the docs into smaller chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
chunks = text_splitter.split_documents(documents=docs)

# Vector embeddings - using free local model
embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

vector_store = QdrantVectorStore.from_documents(
    documents=chunks,
    embedding=embedding_model,
    url="http://localhost:6333",
    collection_name="learning_rag"
)

print("Indexing completed successfully!")