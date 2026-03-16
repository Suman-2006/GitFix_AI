import requests
from backend.config.settings import GITHUB_TOKEN


def create_pull_request(owner, repo, branch, title="AI Generated Fix", body="Fix generated automatically by AI"):

    url = f"https://api.github.com/repos/{owner}/{repo}/pulls"

    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github+json"
    }

    data = {
        "title": title,
        "head": branch,
        "base": "main",
        "body": body
    }

    response = requests.post(url, json=data, headers=headers)

    return response.json()