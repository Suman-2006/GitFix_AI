
import ollama

def generate_fix(issue, context):

    prompt = f"""
Fix the bug in the code.

Issue:
{issue}

Code:
{context}

Return the corrected code.
"""

    response = ollama.chat(
        model="codellama",
        messages=[{"role": "user", "content": prompt}]
    )

    return response["message"]["content"]