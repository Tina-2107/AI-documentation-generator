import ast
from fastapi import HTTPException

def analyze_python_code(code: str):
# handle syntax errors gracefully
    try:
        tree = ast.parse(code)
    except SyntaxError as e:
        raise HTTPException(status_code=400, detail=f"Syntax error in code: {e}")

    functions = []

    classes = []

    imports = []
    
    global_variables = []
    
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            functions.append({
                        "name": node.name,
                        "parameters": [
                                    arg.arg
                                    for arg in node.args.args
                                    ],
                        "docstring": ast.get_docstring(node)
                        })
        elif isinstance(node, ast.ClassDef):
            classes.append(node.name)
        elif isinstance(node, ast.Import):
            for alias in node.names:
                imports.append({
                                "type": "import",
                                "module": alias.name,
                    })
        elif isinstance(node, ast.ImportFrom):
            module = node.module
            for alias in node.names:
                imports.append({
                        "type": "from_import",
                        "module": module,
                        "name": alias.name
                    })
            
    for node in tree.body:
        if isinstance(node, ast.Assign):
            value = None
        try:
            value = ast.unparse(node.value)
        except Exception:
            pass
            for target in node.targets:
                if isinstance(target, ast.Name):
                    global_variables.append({
                    "name": target.id,
                    "value": value
                })

    return {
        "functions": functions,
        "classes": classes,
        "imports": imports,
        "globals": global_variables ,
        
        "function_count": len(functions),
        "class_count": len(classes),
        "import_count": len(imports),
        "global_variable_count": len(global_variables),
    }