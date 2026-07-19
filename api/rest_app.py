"""
SEOS REST API Application.
Exposes SEOS capabilities via HTTP.
"""

from fastapi import FastAPI
from pydantic import BaseModel
from core.kernel import Kernel

app = FastAPI(title="SEOS API", version="1.0.0")

# Inicializar SEOS en memoria de la API
seos_kernel = Kernel()
seos_kernel.initialize()


class ChatRequest(BaseModel):
    message: str


class ReviewRequest(BaseModel):
    file_path: str


@app.get("/")
def read_root():
    return {"status": "ok", "message": "SEOS API is running"}


@app.post("/chat")
def chat_endpoint(request: ChatRequest):
    agent = seos_kernel.agent_manager.get("chat")
    response = agent.execute(request.message)
    return {"response": response}


@app.post("/review")
def review_endpoint(request: ReviewRequest):
    agent = seos_kernel.agent_manager.get("review")
    response = agent.execute(request.file_path)
    return {"review": response}
