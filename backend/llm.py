

import ollama

def analyze_issue_with_ai(issue_text, file_to_fix):

    prompt = f"""
    Analyze this GitHub issue and suggest a fix.

    Issue:
    {issue_text}

    File:
    {file_to_fix}

    Respond in this format:

    Analysis:
    <analysis>

    Fix:
    <code fix>

    Review:
    <review>
    """

    response = ollama.chat(
        model="codellama",
        messages=[{"role": "user", "content": prompt}]
    )

    text = response["message"]["content"]

    return {
        "analysis": text,
        "fix": text,
        "review": text
    }