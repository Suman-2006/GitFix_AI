

import os

def apply_ai_fix(repo_path, file_to_fix, fix_code):

    if not file_to_fix:
        print("ERROR: No file to fix")
        return

    full_path = os.path.join(repo_path, file_to_fix.strip("/"))

    with open(full_path, "w", encoding="utf-8") as f:
        f.write(fix_code)

    print("Fix applied to:", full_path)