from fastapi import FastAPI
from app.routes.upload import router as upload_router
from app.routes.analyze import router as analyze_router
from app.routes.docs import router as docs_router
from app.routes.repository import router as repository_router

app = FastAPI(title="AI Documentation Generator",
    version="0.1.0",
)

@app.get("/")
async def home():
    return {"message": "AI Documentation Generator API"}

@app.get("/about")
async def about():
    return {
"project": "AI Documentation Generator",
"version": "1.0"
}
    
app.include_router(upload_router)

app.include_router(analyze_router)

app.include_router(docs_router)

app.include_router(repository_router)
