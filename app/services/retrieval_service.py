from app.services.embedding_service import EmbeddingService
from app.services.vector_store_service import VectorStoreService
from fastapi import HTTPException

MAX_DISTANCE = 0.8

class RetrievalService:

    def __init__(
        self,
        embedding_service:EmbeddingService,
        vector_store:VectorStoreService
                ):
        self.embedding_service = embedding_service
        self.vector_store = vector_store
        
    def retrieve(
        self,
        query:str,
        project_id:str,
        top_k: int=5,
        ):
        if not query.strip():
            raise HTTPException(status_code=400, detail="question is not given")
        
        query_embedding = self.embedding_service.embed_query(query)
        
        results=self.vector_store.search(
            query_embedding,
            project_id,
            top_k,
        )
        filtered_results = []
        for content, metadata, distance in zip(
        results["documents"][0],
        results["metadatas"][0],
        results["distances"][0],
            ):
            #if distance <= MAX_DISTANCE:
                filtered_results.append({
                "content": content,
                "metadata": metadata,
                "distance": distance,
            })

        return filtered_results