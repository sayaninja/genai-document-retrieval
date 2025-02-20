import fitz  # PyMuPDF for PDF extraction
import os
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, StorageContext, load_index_from_storage
from llama_index.llms.openai import OpenAI
from llama_index.core.node_parser import SimpleNodeParser
from llama_index.core.schema import Document
from llama_index.core.settings import Settings  # ✅ Use new Settings API
from config import OPENAI_API_KEY  # ✅ Import API key from config.py

# Ensure API key is set
if not OPENAI_API_KEY:
    raise ValueError("❌ OpenAI API key is missing! Set it in .env or as an environment variable.")


DATA_DIR = "./data"
STORAGE_DIR = "./storage"

def extract_text_from_pdf(pdf_path):
    """Extracts text from a PDF file using PyMuPDF."""
    doc = fitz.open(pdf_path)
    text = "\n".join([page.get_text("text") for page in doc])
    return text

def load_and_index_documents():
    """Loads documents and indexes them for retrieval."""

    # Ensure storage directory exists
    if not os.path.exists(STORAGE_DIR):
        os.makedirs(STORAGE_DIR)

    # Load documents
    documents = []
    txt_documents = SimpleDirectoryReader(DATA_DIR).load_data()
    documents.extend(txt_documents)

    # Process PDFs correctly
    for file in os.listdir(DATA_DIR):
        if file.endswith(".pdf"):
            pdf_path = os.path.join(DATA_DIR, file)
            text = extract_text_from_pdf(pdf_path)
            if text:
                doc = Document(text=text, metadata={"file_name": file})  # ✅ Convert PDF into Document object
                documents.append(doc)

    if not documents:
        raise ValueError("⚠️ No documents found in 'data/'! Please add PDFs or text files.")

    # Chunk documents into smaller parts for better retrieval
    parser = SimpleNodeParser.from_defaults(chunk_size=512, chunk_overlap=50)
    nodes = parser.get_nodes_from_documents(documents)

    # Set up LLM with new Settings API
    llm = OpenAI(model="gpt-4", temperature=0, api_key=OPENAI_API_KEY)
    Settings.llm = llm  # ✅ New way to set LLM in llama_index

    # Create index
    index = VectorStoreIndex(nodes)

    # Persist index
    index.storage_context.persist(persist_dir=STORAGE_DIR)
    print("✅ Indexed {len(documents)} documents successfully.")

    return index

def query_index(query):
    """Queries the stored index and retrieves relevant content."""

    # Ensure storage exists before querying
    if not os.path.exists(os.path.join(STORAGE_DIR, "docstore.json")):
        print("⚠️ No index found! Creating new index...")
        load_and_index_documents()

    # Load index from storage
    storage_context = StorageContext.from_defaults(persist_dir=STORAGE_DIR)
    index = load_index_from_storage(storage_context)

    # Query and return result
    return index.as_query_engine().query(query)
