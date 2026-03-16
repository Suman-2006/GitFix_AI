import os
from git import Repo

def clone_repo(owner, repo):

    url = f"https://github.com/{owner}/{repo}.git"
    path = f"repos/{repo}"

    if not os.path.exists("repos"):
        os.mkdir("repos")

    if not os.path.exists(path):
        Repo.clone_from(url, path)

    return path

def scan_repo(repo_path):

    detected_files = []

    ignore_dirs = [
        "node_modules",
        ".git",
        "__pycache__",
        "venv",
        ".venv",
        "dist",
        "build"
    ]

    for root, dirs, files in os.walk(repo_path):

        dirs[:] = [d for d in dirs if d not in ignore_dirs]

        for file in files:

            if file.endswith((".js", ".py", ".ts", ".jsx")):

                path = os.path.join(root, file)
                detected_files.append(path.replace(repo_path, ""))

    return detected_files[:50]