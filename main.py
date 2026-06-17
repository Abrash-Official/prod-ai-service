from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Production AI Service"}

@app.post("/v1/rag-query")
def process_document():
    return {"status": "success", "data": "Intern added a new RAG extraction endpoint!"}
