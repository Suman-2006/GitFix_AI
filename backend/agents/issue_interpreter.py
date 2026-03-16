
import ollama
def interpret_issue(issue):

    prompt = f"""
Understand this GitHub issue and explain the required fix.

Issue:
{issue}
"""

    response = ollama.chat(
        model="codellama",
        messages=[{"role": "user", "content": prompt}]
    )

    return response["message"]["content"]