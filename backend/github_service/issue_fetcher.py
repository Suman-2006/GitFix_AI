import requests
from backend.config.settings import GITHUB_TOKEN

def fetch_issue(owner, repo, issue_number):

    url = f"https://api.github.com/repos/{owner}/{repo}/issues/{issue_number}"

    headers = {
        "Authorization": f"token {GITHUB_TOKEN}"
    }

    response = requests.get(url, headers=headers)

    return response.json()