import os
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, StorageContext, load_index_from_storage
from llama_index.llms.openai import OpenAI
from llama_index.core.settings import Settings  # ✅ Use new Settings API
from config import OPENAI_API_KEY  # ✅ Import API key from config.py

# Ensure API key is set
if not OPENAI_API_KEY:
    raise ValueError("❌ OpenAI API key is missing! Set it in .env or as an environment variable.")


DATA_DIR = "./data"
STORAGE_DIR = "./storage"

def load_and_index_documents():
    """Loads documents and indexes them for retrieval."""

    # Ensure storage directory exists
    if not os.path.exists(STORAGE_DIR):
        os.makedirs(STORAGE_DIR)

    # Load documents
    documents = SimpleDirectoryReader(DATA_DIR).load_data()

    # Set up LLM with new Settings API
    llm = OpenAI(model="gpt-4", temperature=0, api_key=OPENAI_API_KEY)
    Settings.llm = llm  # ✅ New way to set LLM in llama_index

    # Create index
    index = VectorStoreIndex.from_documents(documents)

    # Persist index
    index.storage_context.persist(persist_dir=STORAGE_DIR)
    print("✅ Indexing complete! Documents stored successfully.")

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
