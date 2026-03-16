import requests
import os

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

def fetch_issue(owner, repo, issue_number):

    url = f"https://api.github.com/repos/{owner}/{repo}/issues/{issue_number}"

    headers = {
        "Authorization": f"token {GITHUB_TOKEN}"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()

    return {}