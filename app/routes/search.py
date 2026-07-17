from fastapi import APIRouter
from app.services.retrieval_service import RetrievalService
from app.services.embedding_service import EmbeddingService
from app.services.vector_store_service import VectorStoreService
from app.models.search_request import SearchRequest

embedding_service = EmbeddingService()
vector_store = VectorStoreService()

retrival_service= RetrievalService(embedding_service=embedding_service,vector_store=vector_store)

router=APIRouter(
    prefix="/repositories"
)


@router.post("/search")

def retrieval_search(
    request: SearchRequest
    ):
    results=retrival_service.retrieve(
        query=request.question,
        project_id=request.project_id,
        top_k=5,
        )
    return results