from app.services.vector_store_service import VectorStoreService

db = VectorStoreService()

print("Chunks:", db.collection.count())

print()

print(db.collection.get(limit=5))