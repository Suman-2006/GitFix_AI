import os

def scan_repo(repo_path):

    detected_files = []

    for root, dirs, files in os.walk(repo_path):
        for file in files:

            if file.endswith((".js", ".py", ".ts")):

                path = os.path.join(root, file)
                detected_files.append(path.replace(repo_path + "\\", ""))

    return detected_files[:5]