from fastapi import APIRouter, UploadFile,File
from app.services.file_service import save_file

router = APIRouter()

@router.post("/upload_file")
async def upload_file(file: UploadFile = File(...)):
    contents = await file.read()
    text = contents.decode("utf-8")
    lines = text.splitlines()
    path = save_file(file)
    return {
        "filename": file.filename,
        "lines": len(lines),
        "characters": len(text),
        "content": text,
        "size": len(contents),
        "functions_found": text.count("def "),
        "path": str(path)
    }