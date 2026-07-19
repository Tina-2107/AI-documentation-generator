from app.services.rag_service import RAGService

class FakeRetrievalService:

    def retrieve(
        self,
        query,
        project_id,
        top_k,
    ):

        return [
            {
                "content":
                    "def authenticate_user(): pass",

                "metadata": {
                    "file_path":
                        "app/auth.py",

                    "symbol_name":
                        "authenticate_user",

                    "symbol_type":
                        "function",

                    "start_line": 10,

                    "end_line": 20,
                },

                "distance": 0.1,
            }
        ]
        
class FakeLLMService:
    def __init__(self):
        self.received_prompt = None


    def generate_documentation(self, prompt):

        return (
            "Authentication is handled "
            "by authenticate_user()."
        )
        

        
def test_rag_service():
    llm_service=FakeLLMService()
    retrieval_service=FakeRetrievalService()
    
    rag_service = RAGService(
        retrieval_service=retrieval_service,
        llm_service=llm_service,
    )

    result = rag_service.answer_question(
        project_id="test-project",
        question="How is authentication handled?",
        top_k=5,
    )
    assert result["answer"] == (
        "Authentication is handled "
        "by authenticate_user()."
    )
    assert len(result["sources"]) == 1

    assert result["sources"][0] == {
        "file_path": "app/auth.py",
        "symbol_name": "authenticate_user",
        "symbol_type": "function",
        "start_line": 10,
        "end_line": 20,
    }