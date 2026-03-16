import os

def read_file(repo_path, file_path):

    full_path = os.path.join(repo_path, file_path)

    with open(full_path, "r", encoding="utf-8") as f:
        return f.read()