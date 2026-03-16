
import os
from git import Repo

def commit_fix(repo_path, file_path, new_code):

    repo = Repo(repo_path)

    branch = "ai-fix-branch"

    # checkout existing branch if it exists
    if branch in repo.git.branch():
        repo.git.checkout(branch)
    else:
        repo.git.checkout("-b", branch)

    full_path = os.path.join(repo_path, file_path)

    with open(full_path, "w", encoding="utf-8") as f:
        f.write(new_code)

    repo.index.add([file_path])
    repo.index.commit("AI generated fix")

    repo.remote(name="origin").push(branch)

    return branch