from fastapi import APIRouter, UploadFile,File
from app.services.file_service import save_file
from app.utils.file_utils import format_file_size

router = APIRouter()

@router.post("/upload_file")

async def upload_file(file: UploadFile = File(...)):
    contents = await file.read()
    file.file.seek(0) #After reading the file, reset the pointer
    text = contents.decode("utf-8")
    lines = text.splitlines()
    path, extension = save_file(file)
    size_in_bytes = path.stat().st_size 
    return {
        "filename": file.filename,
        "lines": len(lines),
        "characters": len(text),
        "size": format_file_size(size_in_bytes),
        "extension": extension    
    }