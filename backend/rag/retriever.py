import os
from backend.rag.embedder import embed
from backend.rag.vector_store import VectorStore

store = VectorStore()

def build_index(repo_path):

    texts = []

    for root, dirs, files in os.walk(repo_path):

        for f in files:

            if f.endswith(".py") or f.endswith(".js"):

                path = os.path.join(root, f)

                with open(path, "r", errors="ignore") as file:
                    texts.append(file.read())

    embeddings = embed(texts)

    store.build(embeddings, texts)


def retrieve_context(issue):

    q = embed([issue])

    return store.search(q, 3)