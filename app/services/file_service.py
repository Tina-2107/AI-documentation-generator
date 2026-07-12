from pathlib import Path
import shutil
from fastapi import HTTPException, status

UPLOAD_DIR = Path("uploads")
REPOSITORY_UPLOAD_DIR = UPLOAD_DIR / "repositories"

UPLOAD_DIR.mkdir(exist_ok=True)
REPOSITORY_UPLOAD_DIR.mkdir(exist_ok=True)
ALLOWED_EXTENSIONS = {".py",".zip"}

def save_file(upload_file):
    extension = Path(upload_file.filename).suffix.lower()
    #filename = Path(upload_file.filename).name
    if not upload_file.filename:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Filename is missing."
        )
        
    if extension not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid file type. Allowed types are: .py, .zip"
        )
        
    destination = UPLOAD_DIR / Path(upload_file.filename).name
        
    try:
        with destination.open("wb") as buffer:
            shutil.copyfileobj(upload_file.file, buffer)

    except OSError as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to save uploaded file."
        ) from exc

    return destination