from fastapi import FastAPI,UploadFile
from app.routes.upload import router as upload_router
from pydantic import BaseModel
import os

app = FastAPI()

class CodeInput(BaseModel):
    code: str
    
@app.get("/")
async def home():
    return {"message": "AI Documentation Generator API"}

@app.post("/generate-docs")
async def generate_docs(input: CodeInput):
    code = input.code
    documentation = f"This code contains: {code}"
    return {"documentation": documentation}

@app.get("/about")
async def about():
    return {
"project": "AI Documentation Generator",
"version": "1.0"
}
    
app.include_router(upload_router)
    
"""
@app.get("/project_info")
async def project_info():
    files = os.listdir("project")
    file_info = []

    for file in files:
        path = os.path.join("project", file)

        if not os.path.isfile(path):
            continue

        if not file.endswith(".py"):
            continue

        with open(path, "r", encoding="utf-8") as f:
            content = f.read()

        file_info.append({
            "filename": file,
            "lines": len(content.splitlines()),
            "characters": len(content),
            "functions_found": content.count("def ")
        })

    return {"project_files": file_info}
"""