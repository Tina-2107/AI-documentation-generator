from fastapi import APIRouter, UploadFile, File
from pydantic import BaseModel

from app.services.ast_service import analyze_python_code

router = APIRouter()

class CodeRequest(BaseModel):
    code: str

@router.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    code = (await file.read()).decode("utf-8", errors="ignore")
    return analyze_python_code(code)