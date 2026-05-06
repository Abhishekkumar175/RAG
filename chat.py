import os
from dotenv import load_dotenv

from langchain_qdrant import QdrantVectorStore
from langchain_huggingface import HuggingFaceEmbeddings
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GOOGLE_API_KEY"),
    base_url=os.getenv("BASE_URL")
)


# Vector embeddings - using free local model
embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

vector_db = QdrantVectorStore.from_existing_collection(
    embedding=embedding_model,
    url="http://localhost:6333",
    collection_name="learning_rag"
)

#Take user input
user_query = input("Ask something: ")

#Relevent chunks from the vector store
search_results = vector_db.similarity_search(query=user_query)

context = "\n\n\n".join([f"Page Content: {result.page_content}\nPage Number: {result.metadata['page_label']}\nFile Location: {result.metadata['source']}" for result in search_results])

SYSTEM_PROMPT = f"""
You are a helpful AI Assistant who answers user query based on the available
context retrieved from a PDF file along with page_contents and page numbers.

You should only answer the user based on the folowing context and navigate the 
user to open the right page in the PDF file for more information. 
If you don't know the answer, say you don't know.

context:
{context}

"""



response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {   "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": user_query
        }
    ]
)

print(response.choices[0].message.content)