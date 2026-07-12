from pathlib import Path
from app.services.ast_service import analyze_python_code
import json
#context window size for repository analysis
MAX_FILES = 30
MAX_CODE_CHARS_PER_FILE = 6000

def build_repository_context(project_path: Path,
            python_files: list[Path],
        ) -> str:

    """
    Build documentation for the repository based on the analyzed Python files.
    """
    repository_context = []
    python_files = sorted(python_files)

    for file_path in python_files[:MAX_FILES]:
        relative_path = file_path.relative_to(project_path)

        try:
            code = Path(relative_path).read_text(
                encoding="utf-8",
                errors="replace"
            )
            analysis = analyze_python_code(code)
            repository_context.append({
                "file": str(relative_path),
                "analysis": analysis,
                "source_code": code[:MAX_CODE_CHARS_PER_FILE],  # Limit the code length for context
            })
        except SyntaxError as exc:
            repository_context.append({
                "file": str(relative_path),
                "error": f"Syntax error: {exc}"
            })
        except OSError as exc:
            repository_context.append({
                "file": str(relative_path),
                "error": f"Could not read file: {exc}"
            })

    # serialize the repository context to a JSON string with indentation and UTF-8 encoding
    repository_context = json.dumps(
        repository_context,
        indent=2,
        ensure_ascii=False
    )
    return repository_context


