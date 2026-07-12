from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services.pipeline_service import generate_repository_documentation
from app.services.repository_service import extract_zip_file, save_repository_zip,analyze_project

router = APIRouter(
    prefix="/repositories",
    tags=["Repositories"],)

@router.post("/scan")

async def repository_router(file: UploadFile = File(...)):
    """
    Endpoint to upload a ZIP file and scan the extracted project directory.

    Args:
        file: Uploaded ZIP file.
    returns:
        A dictionary containing analysis results.   
    """
    
    saved_file_path = save_repository_zip(file)
    extracted_dir = extract_zip_file(saved_file_path)
    analysis_results = analyze_project(extracted_dir)
    
    return {
    "message": "Repository uploaded and extracted successfully",
    "project": extracted_dir.name,
    "files_found": analysis_results["total_python_files"],
    "analysis": analysis_results
}
    
    
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