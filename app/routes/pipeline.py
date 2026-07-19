from fastapi import APIRouter,HTTPException,UploadFile,File
from app.services.pipeline_service import generate_repository_documentation
from app.services.repository_service import  save_repository_zip

router = APIRouter(
    prefix="/repositories",
    tags=["Repositories"],)

@router.post("/generate-documentation")

async def generate_repository_docs_route(
            file: UploadFile = File(...),):
            
            if not file.filename.endswith(".zip"):
                raise HTTPException(status_code=400, detail="Invalid file format. Please upload a ZIP file.")
            if not file.filename:
                raise HTTPException(status_code=400,             detail="Uploaded file must have a filename",
                    )
            saved_file_path = save_repository_zip(file)
            
            return generate_repository_documentation(saved_file_path)