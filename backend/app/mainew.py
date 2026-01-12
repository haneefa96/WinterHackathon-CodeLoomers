from fastapi import FastAPI
from typing import Dict

app = FastAPI(
    title="CodeLoomers Backend",
    version="0.1.0"
)

@app.get("/", response_model=Dict[str, str])
def root():
    return {"status": "Backend running"}
