# 🧠 GenAI-Powered Document Retrieval System

## 📌 Overview
This project is a **LLM-powered document retrieval system** that allows users to query documents using **natural language prompts**. It leverages **LlamaIndex**, **OpenAI GPT models**, and **FastAPI** to provide an intelligent search experience.

## 🚀 Features
✅ **Semantic Search** - Retrieves relevant documents based on meaning, not just keywords.  
✅ **FastAPI-based API** - Simple RESTful API for querying documents.  
✅ **Vector Storage with LlamaIndex** - Efficient retrieval with embeddings.  
✅ **Supports Multiple Documents** - Index and search through various text files.  

---

## 🛠️ Tech Stack
- **Python** - Backend Language
- **FastAPI** - API Framework
- **LlamaIndex** - Document Indexing & Retrieval
- **OpenAI API** - LLM-powered processing
- **Pinecone/FAISS (Optional)** - Vector Database for embeddings

---

## 📦 Installation

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/YOUR_USERNAME/genai-document-retrieval.git
cd genai-document-retrieval
```

### **2️⃣ Create a Virtual Environment**
```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### **3️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

---

## 🔑 **Setup API Keys**
Create a `.env` file and add your OpenAI API key:
```plaintext
OPENAI_API_KEY=your_openai_api_key
```

Optional: If using Pinecone, add:
```plaintext
PINECONE_API_KEY=your_pinecone_api_key
```

---

## 📂 **Adding Documents**
Place your `.txt` documents in the `data/` directory before running the indexing script.

Example:
```bash
mkdir -p data
echo "This is a sample document for testing." > data/sample.txt
```

---

## ⚡ **Running the Application**
### **1️⃣ Index Documents**
Run:
```bash
PYTHONPATH=src python -c "from retriever import load_and_index_documents; load_and_index_documents()"
```

### **2️⃣ Start FastAPI Server**
```bash
uvicorn src.main:app --reload
```

### **3️⃣ Query the API**
Use `curl` or a browser:
```bash
curl "http://127.0.0.1:8000/query?q=What is this document about?"
```
Response Example:
```json
{
    "response": "This document is about testing the retrieval system."
}
```

---

## 📌 **Next Steps**
✅ Improve search accuracy  
✅ Optimize retrieval performance  
✅ Deploy to AWS/Vercel/DigitalOcean  
✅ Add a frontend interface  

---

## 🤝 **Contributing**
Contributions are welcome! Feel free to fork the repo and submit a PR.

---

## 📜 **License**
This project is licensed under the **MIT License**.
```