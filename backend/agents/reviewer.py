
import ollama
def review_code(code):

    prompt = f"""
Review this code modification.

Code:
{code}

Explain if the fix is correct and suggest improvements.
"""

    response = ollama.chat(
        model="codellama",
        messages=[{"role": "user", "content": prompt}]
    )

    return response["message"]["content"]