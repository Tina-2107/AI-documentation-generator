from pathlib import Path
from app.models.code_chunk import CodeChunk
from app.services.chunking_service import (
    chunk_python_file,
)
from app.services.embedding_service import (
    EmbeddingService,
)
from app.services.vector_store_service import (
    VectorStoreService,
)

from app.services.repository_service import scan_project_directory

embedding_service = EmbeddingService()

vector_store_service = VectorStoreService()

BATCH_SIZE = 32

def generate_repository_chunks(
                    python_files:list[Path],
                    project_root:Path,
                    project_id: str
                    )-> tuple[list[CodeChunk], list[dict]]:
        chunks = []
        errors = []
        for file in python_files:
            try:
                file_chunks= chunk_python_file(
                    file_path=file,
                    project_root=project_root,
                    project_id= project_id
                )
                print("=" * 40)
                print("Type:", type(file))
                print("Value:", file)
                chunks.extend(file_chunks)
    # 3. Skip files that cannot be parsed
            except SyntaxError as exc:
                errors.append({
                    "file":str(file.relative_to(project_root)),
                    "error":str(exc),
                })
                continue
            
        return chunks,errors

def index_repository(
    project_path: Path,
    project_id: str,
):

    # 1. Find Python files
    print("1. Scanning project...")
    python_files=scan_project_directory(project_path)
    print("Done scanning")

    # 2. Generate chunks
    print("2. Generating chunks...")
    chunks,errors=generate_repository_chunks(   
                        python_files=python_files,
                        project_root=project_path,
                        project_id=project_id,
                        )
    print(f"Done chunking. Chunks: {len(chunks)}")
    
    # 4. Generate embeddings
    
    print("3. Generating embeddings...")
    documents = [
                chunk.content
                for chunk in chunks
                ]
    if not chunks:
        return {
                    "project_id": project_id,
                    "files_indexed": 0,
                    "chunks_created": 0,
                    "files_skipped": len(errors),
                    "message": "No indexable Python code found.",
                }
        
    all_embeddings = []

    for i in range(0, len(documents), BATCH_SIZE):

        batch = documents[i:i+BATCH_SIZE]

        try:
            embeddings = embedding_service.embed_documents(batch)

        except Exception as exc:
            return {
                "project_id": project_id,
                "error": f"Embedding generation failed: {exc}"
            }

        all_embeddings.extend(embeddings)
    print("Done embeddings")

    print("4. Deleting old vectors...")
    # 5. Delete old project vectors
    vector_store_service.delete_project(project_id)
    print("Done delete")

    print("5. Upserting vectors...")
    # 6. Upsert current chunks
    vector_store_service.upsert_chunks(chunks,all_embeddings)
    print("Done upsert")
    # 7. Return indexing statistics
    return  {
                "project_id": project_id,
                "files_indexed": len(python_files) - len(errors),
                "chunks_created": len(chunks),
                "files_skipped": len(errors),
                "errors": errors,
                "embedding_model":"all-MiniLM-L6-v2",
                "vector_database": "ChromaDB"
            }