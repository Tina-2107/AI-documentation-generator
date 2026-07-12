from fastapi import APIRouter, File, HTTPException,UploadFile
from app.services.ast_service import analyze_python_code
from app.services.documentation_service import build_file_documentation


router=APIRouter()

@router.post("/generate-documentation", summary="Generate AI documentation from source code")

async def generate(file: UploadFile = File(...)):
    code = (await file.read()).decode("utf-8", errors="ignore")
    if not code.strip():
        raise HTTPException(
            status_code=400,
            detail="Uploaded file is empty."
        )
    result=build_file_documentation(code,file.filename)
    
    return result