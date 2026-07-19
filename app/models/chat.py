from pydantic import BaseModel, Field

class ChatRequest(BaseModel):
    project_id:str = Field(
        min_length=1
    )
    question:str=Field(
        min_length=1,
        max_length=2000
    )
    top_k:int=Field(
        default=5,
        ge=1,
        le=10
    )

class SourceReference(BaseModel):

    file_path: str

    symbol_name: str | None = None

    symbol_type: str | None = None

    start_line: int | None = None

    end_line: int | None = None
    
class ChatResponse(BaseModel):
    answer:str
    sources:list[SourceReference]
    