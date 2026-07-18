import ast
import hashlib
from pathlib import Path

from app.models.code_chunk import CodeChunk

MAX_CHUNK_CHARS = 6000
WINDOW_LINES = 100
OVERLAP_LINES = 20

def create_chunk_id(
        project_id: str,
        file_path: str,
        symbol_type: str,
        symbol_name: str,
        content: str,
    ) -> str:

    raw_value = (
        f"{project_id}:"
        f"{file_path}:"
        f"{symbol_type}:"
        f"{symbol_name}:"
        f"{content}"
    )

    return hashlib.sha256(
        raw_value.encode("utf-8")
    ).hexdigest()


def split_larger_content(content:str,
                    max_chunk_chars,overlap_lines) -> list[str]:
    
    if len(content) <= max_chunk_chars:
        return [content]
    
    lines=content.splitlines(keepends=True)
    
    chunks=[]
    start=0
    
    while start < len(lines):
        current_lines=[]
        current_length=0
        end=start
        
        while end < len(lines):

                    line = lines[end]

                    if current_length + len(line) > max_chunk_chars:
                        break

                    current_lines.append(line)
                    current_length += len(line)
                    end += 1
        # One individual line is larger than the limit
        if end==start:
            chunks.append(lines[start][:max_chunk_chars])
            start+=1
            continue
        
        chunks.append("".join(current_lines))
        
        if end == len(lines):
            break
        
        start = max(end - overlap_lines, start + 1)
        
    return chunks

def create_symbol_chunks(
            *,
            source: str,
            node: ast.FunctionDef
                | ast.AsyncFunctionDef
                | ast.ClassDef,
            project_id: str,
            relative_path: str,
            symbol_type: str,
        ) -> list[CodeChunk]:

    content = ast.get_source_segment(source, node)
    if content is None:
        content = ast.unparse(node)
    parts = split_larger_content(content,MAX_CHUNK_CHARS,OVERLAP_LINES)

    chunks = []

    for part_index, part_content in enumerate(parts):

        chunk_id = create_chunk_id(
            project_id=project_id,
            file_path=relative_path,
            symbol_type=symbol_type,
            symbol_name=node.name,
            content=part_content,
        )

        chunks.append(
            CodeChunk(
                id=chunk_id,
                content=part_content,
                metadata={
                    "project_id": project_id,
                    "file_path": relative_path,
                    "symbol_name": node.name,
                    "symbol_type": symbol_type,
                    "start_line": node.lineno,
                    "end_line": node.end_lineno,
                    "part_index": part_index,
                    "part_count": len(parts),
                    "language": "python",
                    "chunk_type": "code",
                },
            )
        )

    return chunks


def chunk_python_file(
            file_path: Path,
            project_root: Path,
            project_id: str,
        ) -> list[CodeChunk]:

    source = file_path.read_text(
        encoding="utf-8",
        errors="replace",
    )

    tree = ast.parse(source)

    chunks = []
    module_nodes: list[ast.AST] = []

    relative_path = str(
        file_path.relative_to(project_root)
    )

    for node in tree.body:
        # chunk import statements and module-level assignments as a single chunk
        if isinstance(node, (ast.Import, ast.ImportFrom,ast.Assign , ast.AnnAssign)):
            module_nodes.append(node)
        
        # chunk function 
        elif isinstance(node,(ast.FunctionDef, ast.AsyncFunctionDef)):

            content = ast.get_source_segment(
                source,
                node,
            )
            if content is None:
                content= ast.unparse(node)
            
            symbol_type = (
                "async_function"
                if isinstance(node, ast.AsyncFunctionDef)
                else "function"
            )
            chunks.extend(
                create_symbol_chunks(
                    source=source,
                    node=node,
                    project_id=project_id,
                    relative_path=relative_path,
                    symbol_type=symbol_type,
                )
            )

        # chunk class
        elif isinstance(node, ast.ClassDef):
            content = ast.get_source_segment(source,
                node,)
            
            symbol_type="class"
            chunks.extend(
                create_symbol_chunks(
                    source=source,
                    node=node,
                    project_id=project_id,
                    relative_path=relative_path,
                    symbol_type=symbol_type,
                )
            )

            
    if module_nodes:
            module_parts=[ ast.get_source_segment(source, node)
            for node in module_nodes
        ]
            
            module_content = "\n".join(module_parts)
            module_chunk_id = create_chunk_id(
                project_id,
                relative_path,
                "module",
                relative_path,
                module_content,
            )
            chunks.append(
                CodeChunk(
                    id=module_chunk_id,
                    content=module_content,
                    metadata={
                        "project_id": project_id,
                        "file_path": relative_path,
                        "symbol_name": relative_path,
                        "symbol_type": "module",
                    },
                )
            )
    return chunks