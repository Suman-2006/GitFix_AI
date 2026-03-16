from sentence_transformers import SentenceTransformer

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

def embed(texts):
    """
    Convert text or list of texts into embeddings
    """

    if isinstance(texts, str):
        texts = [texts]

    return model.encode(texts)