from pathlib import Path
import shutil
from fastapi import HTTPException, status

UPLOAD_DIR = Path("uploads")

UPLOAD_DIR.mkdir(exist_ok=True)
ALLOWED_EXTENSIONS = {".py",".zip"}

def save_file(upload_file):
    extension = Path(upload_file.filename).suffix.lower()
    if extension not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid file type. Allowed types are: .py, .js, .java, .cpp"
        )
    filename = Path(upload_file.filename).name
    destination = UPLOAD_DIR / filename

    with destination.open("wb") as buffer:
        shutil.copyfileobj(upload_file.file, buffer)

    return destination,extension