from fastapi import APIRouter
from app.models.chat import(
    ChatRequest,
    ChatResponse,
)
from app.services.rag_service import RAGService
from app.services.embedding_service import EmbeddingService
from app.services.vector_store_service import VectorStoreService
from app.services.retrieval_service import RetrievalService
from app.services.llm_service import LLMService

# Create dependencies
embedding_service = EmbeddingService()

vector_store = VectorStoreService()

retrieval_service = RetrievalService(
    embedding_service=embedding_service,
    vector_store=vector_store,
)

llm_service = LLMService()

rag_service = RAGService(
    retrieval_service=retrieval_service,
    llm_service=llm_service,
)

router=APIRouter(
    prefix="/repositories",
    tags=["Codebase Chat"],
)

@router.post("/chat",response_model=ChatResponse,)

def chat(request:ChatRequest):
    result=rag_service.answer_question(
        project_id=request.project_id,
        question=request.question,
        top_k=request.top_k,
    )

    return result