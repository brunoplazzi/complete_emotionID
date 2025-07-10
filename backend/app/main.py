from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image as PILImage
from io import BytesIO
import numpy as np

from app.processamento import Imagem  # ajuste conforme sua estrutura

app = FastAPI()

# Middleware CORS para aceitar requisições de qualquer origem (ideal para testes)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/analisa")
async def analisa(file: UploadFile = File(...)):
    try:
        conteudo = await file.read()
        imagem_pil = PILImage.open(BytesIO(conteudo)).convert("RGB")
    except Exception:
        return JSONResponse(content={"erro": "Arquivo inválido ou não é uma imagem."}, status_code=400)

    imagem_np = np.array(imagem_pil)

    face = Imagem.detectar_face(imagem_np)
    if face is None:
        return JSONResponse(content={"erro": "Nenhum rosto detectado."}, status_code=400)

    try:
        resultado = Imagem.identificar_emocao(face)
        return JSONResponse(content=resultado)
    except Exception as e:
        return JSONResponse(content={"erro": f"Erro ao analisar emoção: {str(e)}"}, status_code=500)
