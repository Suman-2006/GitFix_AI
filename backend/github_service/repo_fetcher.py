
from git import Repo
import os
from backend.config.settings import GITHUB_TOKEN

def clone_repo(owner, repo):

    repo_url = f"https://{GITHUB_TOKEN}@github.com/{owner}/{repo}.git"

    local_path = f"repos/{repo}"

    if not os.path.exists("repos"):
        os.mkdir("repos")

    if not os.path.exists(local_path):
        Repo.clone_from(repo_url, local_path)

    return local_path