from pathlib import Path
import shutil
from fastapi import HTTPException, status

UPLOAD_DIR = Path("uploads")

UPLOAD_DIR.mkdir(exist_ok=True)
ALLOWED_EXTENSIONS = {".py", ".js", ".java", ".cpp",".zip"}

def save_file(upload_file):
    extension = Path(upload_file.filename).suffix
    if extension not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid file type. Allowed types are: .py, .js, .java, .cpp"
        )

    destination = UPLOAD_DIR / upload_file.filename

    with destination.open("wb") as buffer:
        shutil.copyfileobj(upload_file.file, buffer)

    return destination,extension