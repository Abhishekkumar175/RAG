# RAG Repository

A Python-based **Retrieval-Augmented Generation (RAG)** project implementing two different RAG architectures:

- **Traditional RAG** – Standard indexing and retrieval workflow  
- **Async RAG** – Asynchronous pipeline for scalable and faster document retrieval

This project demonstrates how Large Language Models (LLMs) can generate accurate and context-aware responses using semantic search and document retrieval techniques.

---

## Features

- Traditional RAG implementation
- Async RAG pipeline
- Document indexing and retrieval
- PDF document processing
- Chat-based querying system
- Docker support for deployment

---

## Project Structure

```bash
.
├── Async-RAG/          # Async RAG implementation
├── chat.py             # Retrieval and chat workflow
├── index.py            # Traditional indexing pipeline
├── docker-compose.yml  # Docker configuration
├── requirements.txt    # Dependencies
└── JD_Cognizant Ace Team program.pdf
```

---

## Tech Stack

- Python
- Retrieval-Augmented Generation (RAG)
- Vector Embeddings
- Async Processing
- Docker

---

## Getting Started

### Clone the Repository

```bash
git clone <your-repo-url>
cd RAG
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Traditional RAG

Run the indexing pipeline:

```bash
python index.py
```

Start the chat/retrieval system:

```bash
python chat.py
```

---

## Async RAG

Navigate to the async implementation:

```bash
cd Async-RAG
```

Run the async workflow based on your setup.

---

## Objective

The goal of this repository is to explore and compare **Traditional RAG** and **Async RAG** architectures for efficient document retrieval and LLM-powered question answering systems.

---

## Future Improvements

- Add vector database integration
- Support multiple document formats
- Improve retrieval accuracy
- Add frontend UI
- Deploy with cloud services

---

## Author

**Abhishekkumar175**
