"""
SEOS REST API Application.
Exposes SEOS capabilities via HTTP with optional API Key authentication.
"""

from fastapi import FastAPI, Security, HTTPException, status
from fastapi.security import APIKeyHeader
from pydantic import BaseModel
from core.kernel import Kernel
from config.settings import Settings

app = FastAPI(title="SEOS API", version="2.0.0")

# Inicializar SEOS en memoria de la API
seos_kernel = Kernel()
seos_kernel.initialize()

# Configuración de Seguridad
api_key_header = APIKeyHeader(name="X-API-Key", auto_error=False)


async def verify_api_key(api_key: str = Security(api_key_header)):
    # Si no hay SEOS_API_KEY configurada en el .env, el acceso es libre (modo local)
    if not Settings.SEOS_API_KEY:
        return api_key
    # Si está configurada, exigimos que coincida
    if api_key == Settings.SEOS_API_KEY:
        return api_key
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid or missing API Key. Provide it in the 'X-API-Key' header.",
    )


class ChatRequest(BaseModel):
    message: str


class ReviewRequest(BaseModel):
    file_path: str


@app.get("/", dependencies=[Security(verify_api_key)])
def read_root():
    return {"status": "ok", "message": "SEOS API is running"}


@app.post("/chat", dependencies=[Security(verify_api_key)])
def chat_endpoint(request: ChatRequest):
    agent = seos_kernel.agent_manager.get("chat")
    response = agent.execute(request.message)
    return {"response": response}


@app.post("/review", dependencies=[Security(verify_api_key)])
def review_endpoint(request: ReviewRequest):
    agent = seos_kernel.agent_manager.get("review")
    response = agent.execute(request.file_path)
    return {"review": response}
