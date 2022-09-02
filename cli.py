import subprocess
import os

# This is our shell command, executed in subprocess.
os.chdir("src/backend_src")
p = subprocess.run(["python3", "manage.py", "runserver"])
