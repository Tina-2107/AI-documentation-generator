from pydantic import BaseModel

class SearchRequest(BaseModel):
    project_id:str
    question:str

