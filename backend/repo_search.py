import os
import numpy as np

from backend.embeddings import embed
from backend.chunker import chunk_code


def find_relevant_file(repo_path, files, issue_text):

    all_chunks = []
    file_map = []

    for file in files:
        try:
            path = os.path.join(repo_path, file.strip("/"))

            with open(path, "r", encoding="utf-8") as f:
                code = f.read()

            chunks = chunk_code(code)

            for chunk in chunks:
                all_chunks.append(chunk)
                file_map.append(file)

        except:
            pass

    if not all_chunks:
        return None

    issue_embedding = embed(issue_text)
    chunk_embeddings = embed(all_chunks)

    scores = np.dot(chunk_embeddings, issue_embedding.T)

    best_index = scores.argmax()

    return file_map[best_index]