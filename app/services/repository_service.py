import zipfile
from pathlib import Path

from app.services.ast_service import analyze_python_code

EXTRACT_DIR = Path("extracted_projects")

EXTRACT_DIR.mkdir(parents=True, exist_ok=True)

# Ignore these folders while scanning
IGNORE_FOLDERS = {
    "__pycache__",
    ".git",
    "venv",
    "node_modules"
}


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
    analysis = {
        "project_name": project_dir.name,
        "total_python_files": len(python_files),
        "python_files": python_files
    }
    for file in python_files:
        text = file.read_text(encoding="utf-8",errors="ignore")
        analysis["python_files"].append({
            "name": file.name,
            "path": str(file.relative_to(project_dir)),
            "analysis": analyze_python_code(text)
        })
    return analysis