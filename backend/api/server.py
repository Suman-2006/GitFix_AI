
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# your imports


from backend.github_service.issue_fetcher import fetch_issue
from backend.github_service.repo_fetcher import clone_repo
from backend.github_service.repo_scanner import scan_repo
from backend.repo_search import find_relevant_file
from backend.llm import analyze_issue_with_ai
from backend.fixer import apply_ai_fix
from backend.github_service.code_committer import commit_fix
from backend.github_service.pr_creator import create_pull_request

# from github_service.issue_fetcher import fetch_issue
# from github_service.repo_fetcher import clone_repo
# from github_service.repo_scanner import scan_repo
# from repo_search import find_relevant_file
# from llm import analyze_issue_with_ai
# from fixer import apply_ai_fix
# from github_service.code_committer import commit_fix
# from github_service.pr_creator import create_pull_request
app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "API running"}

@app.post("/analyze")
def analyze(data: dict):

    owner = data.get("owner")
    repo = data.get("repo")
    issue_number = data.get("issue")

    print("STEP 1: request received")

    issue = fetch_issue(owner, repo, issue_number)
    print("STEP 2: issue fetched")

    issue_title = issue.get("title", "")
    issue_body = issue.get("body", "")
    issue_text = f"{issue_title}\n\n{issue_body}"

    repo_path = clone_repo(owner, repo)
    print("STEP 3: repo cloned")

    files = scan_repo(repo_path)
    print("STEP 4: repo scanned")

    file_to_fix = find_relevant_file(repo_path, files, issue_text)
    print("STEP 5: relevant file found")

    ai_result = analyze_issue_with_ai(issue_text, file_to_fix)
    print("STEP 6: AI finished")

    analysis = ai_result["analysis"]
    fix_code = ai_result["fix"]
    review = ai_result["review"]

    apply_ai_fix(repo_path, file_to_fix, fix_code)
    print("STEP 7: fix applied")

    branch = commit_fix(repo_path, file_to_fix, "AI fix")
    print("STEP 8: committed")

    pr = create_pull_request(owner, repo, branch)
    print("STEP 9: PR created")

    return {
        "issue": issue_text,
        "analysis": analysis,
        "fix": fix_code,
        "review": review,
        "pull_request": pr.get("html_url")
    }
