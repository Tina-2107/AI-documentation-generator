from fastapi import APIRouter, UploadFile, File, HTTPException
from pathlib import Path
from app.services.file_service import save_file
from app.services.repository_service import extract_zip_file,scan_project_directory,analyze_project

router = APIRouter()

@router.post("/scan-project")

async def repository_router(file: UploadFile = File(...)):
    """
    Endpoint to upload a ZIP file and scan the extracted project directory.

    Args:
        file: Uploaded ZIP file.
    returns:
        A dictionary containing analysis results.   
    """
    saved_file_path = save_file(file)
    if not file.filename.lower().endswith(".zip"):
        raise HTTPException(status_code=400, detail="Invalid file format. Please upload a ZIP file.")
    extracted_dir = extract_zip_file(saved_file_path)
    scan_results = scan_project_directory(extracted_dir)
    analysis_results = analyze_project(extracted_dir)
    
    return {
    "project": extracted_dir.name,
    "files_found": len(scan_results),
    "analysis": analysis_results
}