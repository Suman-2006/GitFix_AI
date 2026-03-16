import faiss
import numpy as np

class VectorStore:

    def __init__(self):
        self.index = None
        self.texts = []

    def build(self, embeddings, texts):

        dim = len(embeddings[0])
        self.index = faiss.IndexFlatL2(dim)

        self.index.add(np.array(embeddings))

        self.texts = texts

    def search(self, query_vector, k=3):

        D, I = self.index.search(query_vector, k)

        return [self.texts[i] for i in I[0]]