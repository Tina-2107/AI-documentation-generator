from pathlib import Path
from app.services.llm_service import generate_documentation

PROMPT_FILE_PATH = Path("prompts/documentation_prompt.txt")

OUTPUT=Path("generated_docs")
OUTPUT.mkdir(exist_ok=True)

def format_summary(summary: dict) -> str:
    text = ""
    text += "Functions:\n"

    for func in summary.get("functions", []):
        text += f"- {func['name']}({', '.join(func['parameters'])})\n"
    text += "\nClasses:\n"

    for cls in summary.get("classes", []):
        text += f"- {cls}\n"
    text += "\nImports:\n"

    for imp in summary.get("imports", []):
        text += f"- {imp}\n"
    return text

def build_documentation(code,code_summary,filename):
    template=PROMPT_FILE_PATH.read_text()
    prompt=template.replace("{{CODE}}",code)
    summary_text = format_summary(code_summary)
    prompt = prompt.replace(
        "{{CODE_SUMMARY}}",
        summary_text
        )
    documentation = generate_documentation(prompt)
    file_name = Path(filename).stem
    output_file =OUTPUT/f"{file_name}_documentation.md"
    output_file .write_text(documentation,encoding="utf-8")
    
    return {
        "documentation": documentation,
        "file_path": str(output_file )
    }