from pathlib import Path
from app.services.ast_service import analyze_python_code
from app.services.llm_service import generate_documentation

PROMPT_FILE_PATH = Path("prompts/documentation_prompt.txt")

PROMPT_REPOSITORY_PATH = Path("prompts/repository_documentation_prompt.txt")

OUTPUT=Path("generated_docs")
OUTPUT.mkdir(exist_ok=True)

def format_summary(summary: dict) -> str:
    text = ""
    
    text += "Functions:\n"
    for func in summary.get("functions", []):
        text += f"- {func['name']}({', '.join(func['parameters'])})\n"
    
    text += "\nClasses:\n"
    for cls in summary.get("classes", []):
        text += f"- {cls['name']}\n"
    
    text += "\nImports:\n"
    for imp in summary.get("imports", []):
        text += f"- {imp['module']}\n"
        
    text += "\nGlobal Variables:\n"
    for var in summary.get("globals", []):
        text += f"- {var['name']}: {var['value']}\n"
        
    return text

def build_file_documentation(code,filename):
    template=PROMPT_FILE_PATH.read_text()
    code_summary = analyze_python_code(code)
    prompt = template.replace(
        "{{analysis}}", format_summary(code_summary)
    ).replace(
        "{{code}}", code
    )
    documentation = generate_documentation(prompt)
    file_name = Path(filename).stem
    output_file =OUTPUT/f"{file_name}_documentation.md"
    output_file .write_text(documentation,encoding="utf-8")
    
    return {
        "documentation": documentation,
        "file_path": str(output_file )
    }
    
def generate_repository_docs(repository_context, zip_filename):
        """
        Generate documentation for the entire repository based on the analyzed context.
        """
        template = PROMPT_REPOSITORY_PATH.read_text()
        prompt = template.replace(
            "{{REPOSITORY_CONTEXT}}", repository_context
            # No specific code to include for the entire repository
                    )
        documentation = generate_documentation(prompt)
        
        file_name = Path(zip_filename).stem
        output_file = OUTPUT / f"{file_name}_repository_documentation.md"
        output_file.write_text(documentation, encoding="utf-8")
        
        return {
            "documentation": documentation,
            "file_path": str(output_file)
        }           