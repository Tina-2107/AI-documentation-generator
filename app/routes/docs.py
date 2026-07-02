from fastapi import APIRouter, File,UploadFile
from app.services.ast_service import analyze_python_code
from app.services.llm_service import generate_documentation
#from app.routes.analyze import analyze

router=APIRouter()

@router.post("/generate-documentation")

async def generate(file: UploadFile = File(...)):
    code = (await file.read()).decode("utf-8", errors="ignore")
    analysis=analyze_python_code(code)
    prompt = f"""
        You are a senior Python software engineer.
        Generate professional Markdown documentation.
        Include:
        # Overview
        # Classes
        # Functions
        # Parameters
        # Return Values
        # Imports
        Do not invent information.
        Use only the following analysis:

        {analysis}
        """
    documentation=generate_documentation(prompt)
    
    return {"documentation":documentation}