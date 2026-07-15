from fastapi import APIRouter, File,UploadFile
from app.services.indexing_service import index_repository
from app.services.repository_service import save_repository_zip,extract_zip_file


router=APIRouter( prefix="/repositories",
    tags=["Repository Indexing"]
    )

@router.post("/index", summary="Generate indexing Repository")

async def indexing_repository(file: UploadFile = File(...)):
    print("Route started")

    saved_file_path = save_repository_zip(file)
    print("ZIP saved")
    extracted_dir = extract_zip_file(saved_file_path)
    print("ZIP extracted")

    project_id = extracted_dir.name
    print("Calling index_repository...")
    index_response=index_repository(extracted_dir,project_id)
    print(index_response)
    return index_response