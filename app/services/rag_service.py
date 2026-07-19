from pathlib import Path


PROMPT_PATH = Path(
    "prompts/codebase_qa_prompt.txt"
)
def build_prompt(
    question:str,
    context:str,
    ):
    template=PROMPT_PATH.read_text(encoding="utf-8")
    template=template.replace(
        "{{QUESTION}}",
            question,
        ).replace(
            "{{CONTEXT}}",
            context,
        )
        
    return template
    
def build_context(results):
    sections=[]
    for index, result in enumerate(
        results,
        start=1,
    ):
        metadata=result["metadata"]
        
        section = f"""
--- SOURCE {index} ---

File: {metadata.get("file_path")}
Symbol: {metadata.get("symbol_name")}
Type: {metadata.get("symbol_type")}
Lines: {metadata.get("start_line")} - {metadata.get("end_line")}

Code:
{result["content"]}
"""
        sections.append(section)
        
    return "\n".join(sections)

#dependency injection
class RAGService:

    def __init__(
        self,
        retrieval_service,
        llm_service,
    ):
        self.retrieval_service = retrieval_service
        self.llm_service = llm_service
        
    def answer_question(
        self,
        project_id: str,
        question: str,
        top_k: int = 5,
        ):
        results=self.retrieval_service.retrieve(
            query=question,
            project_id=project_id,
            top_k=top_k,
        )
        print("RAG RECEIVED RESULTS:", len(results))
        if not results:
            return {
                "answer":
                    "I could not find relevant indexed code "
                    "for this question.",

                "sources": []
            }
        context=build_context(results)
        
        prompt=build_prompt(question,context)
        
        answer = self.llm_service.generate_documentation(prompt)
        
        source_list=[]
        
        for result in results:
            metadata = result["metadata"]
            source_list.append({
                "file_path":
                    metadata.get("file_path"),
                "symbol_name":
                    metadata.get("symbol_name"),
                "symbol_type":
                    metadata.get("symbol_type"),
                "start_line":
                    metadata.get("start_line"),
                "end_line":
                    metadata.get("end_line"),
            })
        return {
            "answer": answer,
            "sources": source_list,
        }   