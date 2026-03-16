from fastapi import FastAPI
from github_service.repo_fetcher import fetch_repo
from github_service.issue_fetcher import fetch_issue
from rag.retriever import build_index, retrieve_context
from agents.issue_interpreter import interpret_issue
from agents.code_modifier import generate_fix
from agents.reviewer import review_code

app = FastAPI()


@app.post("/analyze")

def analyze(data: dict):

    owner = data["owner"]
    repo = data["repo"]
    issue_number = data["issue"]

    repo_path = fetch_repo(owner, repo)

    issue = fetch_issue(owner, repo, issue_number)

    issue_text = issue["title"] + "\n" + issue["body"]

    analysis = interpret_issue(issue_text)

    build_index(repo_path)

    context = retrieve_context(issue_text)

    fix = generate_fix(issue_text, context)

    review = review_code(fix)

    return {
        "issue": issue_text,
        "analysis": analysis,
        "fix": fix,
        "review": review
    }