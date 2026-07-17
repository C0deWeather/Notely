"""This script pushes a commit to GitHub"""

import sys
import subprocess

try:
    if sys.argv[1] != "-m":
        print("hint: addcommit -m <commit message> <files>")
        sys.exit(1)

    commit_message = sys.argv[2]
except IndexError:
    print("missing commit message")
    sys.exit(1)

files = sys.argv[3:]

if not files:
    print("hint: addcommit -m <commit message> <files>")
    sys.exit(1)

try:
    subprocess.run(["git", "add", *files], check=True)
    subprocess.run(["git", "commit", "-m", commit_message], check=True)
    subprocess.run(["git", "push"], check=True)
except subprocess.CalledProcessError:
    sys.exit(1)
