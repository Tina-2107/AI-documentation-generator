import shutil
import zipfile
from fastapi import UploadFile,HTTPException,status
from pathlib import Path
from app.services.ast_service import analyze_python_code

REPOSITORY_UPLOAD_DIR = Path("uploads/repositories")
EXTRACT_DIR = Path("extracted_projects")

REPOSITORY_UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
EXTRACT_DIR.mkdir(parents=True, exist_ok=True)

# Ignore these folders while scanning
IGNORE_FOLDERS = {
    "__pycache__",
    ".git",
    "venv",
    "node_modules"
}

def save_repository_zip(file: UploadFile) -> Path:
    if not file.filename:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Filename is missing",
        )

    filename = Path(file.filename).name

    if Path(filename).suffix.lower() != ".zip":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Only ZIP repositories are supported",
        )

    destination = REPOSITORY_UPLOAD_DIR / filename

    with destination.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return destination

def extract_zip_file(zip_path:Path)->Path:
    """
    Extract a ZIP archive into the extracted_projects directory.

    Args:
        zip_path: Path to the uploaded ZIP file.

    Returns:
        Path to the extracted project directory.
    """
    project_dir=EXTRACT_DIR / zip_path.stem
    extract_dir = project_dir
    counter=1
    while extract_dir.exists():
        extract_dir = EXTRACT_DIR / f"{zip_path.stem}_{counter}"
        counter+=1
        
    extract_dir.mkdir(parents=True, exist_ok=True)

    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall(extract_dir)

    return extract_dir #return extract_dir.resolve()



def scan_project_directory(project_dir: Path) -> list:
    python_files = []
    for file in project_dir.rglob("*.py"):
        if not any(folder in file.parts for folder in IGNORE_FOLDERS):
            python_files.append(file)
    return python_files


def analyze_project(project_dir: Path) -> dict:
    """
    Analyze the extracted project directory.

    Args:
        project_dir: Path to the extracted project directory.

    Returns:
        A dictionary containing analysis results.
    """
    python_files = scan_project_directory(project_dir)
    analyzed_files = []
    for file_path in python_files:
        code = file_path.read_text(encoding="utf-8",errors="ignore")
        
        file_analysis = analyze_python_code(code)

        analyzed_files.append({
            "name": file_path.name,
            "path": str(file_path.relative_to(project_dir)),
            "analysis": file_analysis,
        })

    return {
        "project_name": project_dir.name,
        "total_python_files": len(python_files),
        "python_files": analyzed_files,
    }