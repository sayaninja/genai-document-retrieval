import sys
import os

# Ensure Python finds the src directory
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from retriever import query_index
from fastapi import FastAPI

app = FastAPI()

@app.get("/query")
async def query_llm(q: str):
    response = query_index(q)
    return {"response": response}
