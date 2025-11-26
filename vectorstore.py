import numpy as np
import faiss
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")


def build_vector_store(questions):
    # we embed the question text field
    texts = [q["question"] for q in questions]
    embeddings = model.encode(texts)
    embeddings = np.array(embeddings).astype("float32")

    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)

    # return index + the original question dicts (id, domain, etc.)
    return index, questions


def search_similar(query, index, questions, top_k: int = 3):
    q_emb = model.encode([query]).astype("float32")
    D, I = index.search(q_emb, top_k)
    return [questions[i] for i in I[0]]
