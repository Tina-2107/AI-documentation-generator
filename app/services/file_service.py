from pathlib import Path
import shutil
#Save Uploaded Files
UPLOAD_DIR = Path("uploads")

UPLOAD_DIR.mkdir(exist_ok=True)


def save_file(upload_file):

    destination = UPLOAD_DIR / upload_file.filename

    with destination.open("wb") as buffer:
        shutil.copyfileobj(upload_file.file, buffer)

    return destination