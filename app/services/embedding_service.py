from sentence_transformers import SentenceTransformer

DEFAULT_MODEL = "all-MiniLM-L6-v2"

class EmbeddingService:
    #contructor for load one time
    def __init__(self):

        self.model = SentenceTransformer(
        DEFAULT_MODEL
        )
    # returns something conceptually One vector per document and stored in chromaDB
    def embed_documents(self,
                        documents: list[str],
                        )-> list[list[float]]:
        embeddings = self.model.encode(
            documents,
            batch_size=32,
            show_progress_bar=False,
            normalize_embeddings=True,
        )

        return embeddings.tolist()
    
        # returns something conceptually One vector per query and search in chromaDB
    def embed_query(
        self,
        query: str,
    ) -> list[float]:

        embedding = self.model.encode(
            query,
            normalize_embeddings=True,
        )

        return embedding.tolist()



embedding_service = EmbeddingService()