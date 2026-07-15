from sentence_transformers import SentenceTransformer
import time

print("Loading model...")
model = SentenceTransformer("all-MiniLM-L6-v2")
print("Model loaded")

documents = [
    "def add(a, b): return a + b",
    "class User:",
    "DATABASE_URL = 'sqlite://'",
    "def login(username): pass",
    "async def fetch_data(): pass",
    "app = FastAPI()",
    "PI = 3.14"
]

print("Starting encode...")
start = time.time()

embeddings = model.encode(
    documents,
    normalize_embeddings=True,
)

print("Finished")
print("Shape:", embeddings.shape)
print("Time:", time.time() - start)