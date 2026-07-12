from pathlib import Path
from app.services.documentation_service import generate_repository_docs
from app.services.repository_service import extract_zip_file, scan_project_directory
from app.services.context_service import build_repository_context, MAX_FILES


def generate_repository_documentation(zip_path: Path):
    """
    Coordinate repository analysis and documentation generation.
    """
    
    try:
        extracted_path = extract_zip_file(zip_path)
        
        python_files=scan_project_directory(extracted_path)
        
        repository_context = build_repository_context(extracted_path, python_files)
        
        result = generate_repository_docs(repository_context,zip_path.name)
        
        output_file =result["file_path"]
        
    finally:
        if zip_path.exists():
            zip_path.unlink() # Clean up the uploaded zip file after processing
    return  {
            "project_name": zip_path.stem,
            "files_analyzed": len(python_files),
            "files_processed": min(
                    len(python_files),
                    MAX_FILES,
                ),
            "documentation_path": output_file
        }