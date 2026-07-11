import ast
from fastapi import HTTPException

def extract_function(node):
    return {
        "name": node.name,
        "parameters": [
            arg.arg for arg in node.args.args
        ],
        "docstring": ast.get_docstring(node),
        "is_async": isinstance(node, ast.AsyncFunctionDef),
    }



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
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)
        ):
            functions.append(extract_function(node))

        elif isinstance(node, ast.ClassDef):
            class_info = {
                "name": node.name,
                "docstring": ast.get_docstring(node),
                "methods": [],
            }

            for item in node.body:

                if isinstance(
                    item,
                    (ast.FunctionDef, ast.AsyncFunctionDef)
                ):
                    class_info["methods"].append(
                        extract_function(item)
                    )
            classes.append(class_info)
            
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
            for target in node.targets:
                if isinstance(target, ast.Name):
                    global_variables.append({
                        "name": target.id,
                        "value": ast.unparse(node.value)
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