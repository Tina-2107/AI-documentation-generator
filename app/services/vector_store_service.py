from pathlib import Path

import chromadb

from app.models.code_chunk import CodeChunk


CHROMA_DIR = Path("chroma_data")
CHROMA_DIR.mkdir(
    parents=True,
    exist_ok=True,
)
COLLECTION_NAME = "code_chunks"

class VectorStoreService:

    def __init__(self):

        self.client = chromadb.PersistentClient(
            path=str(CHROMA_DIR)
        )

        self.collection = (
            self.client.get_or_create_collection(
                name=COLLECTION_NAME
            )
        )


    def upsert_chunks(
                self,
                chunks: list[CodeChunk],
                embeddings: list[list[float]],
            ) -> None:

        if not chunks:
            return
        
        if len(chunks) != len(embeddings):
            raise ValueError(
                "Chunks and embeddings must have the same length."
            )
        try:
            self.collection.upsert(
                ids=[
                    chunk.id
                    for chunk in chunks
                ],
                documents=[
                    chunk.content
                    for chunk in chunks
                ],
                metadatas=[
                    chunk.metadata
                    for chunk in chunks
                ],
                embeddings=embeddings,
            )
        
        except Exception as exc:
            raise RuntimeError(
                f"Failed to store vectors: {exc}"
            )
                
    def delete_project(self,project_id:str) -> None:
        self.collection.delete(
            where={
                "project_id" :project_id
            }
        )
        
    def search(
                self,
                query_embedding: list[float],
                project_id: str,
                top_k: int = 5,
            ):
        return self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k,
            where={
                "project_id": project_id
            }
        )