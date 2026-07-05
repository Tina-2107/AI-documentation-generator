from fastapi import FastAPI
from app.routes.upload import router as upload_router
from pydantic import BaseModel
from app.routes.analyze import router as analyze_router
from app.routes.docs import router as docs_router
from app.routes.repository import router as repository_router

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

app.include_router(analyze_router)

app.include_router(docs_router)

app.include_router(repository_router, prefix="/analyze", tags=["Analyze"])