import subprocess


message = "initial commit from gh:zehengl/cookiecutter-heroku-flask"

subprocess.call(["git", "init"])
subprocess.call(["git", "add", "*"])
subprocess.call(["git", "commit", "-m", message])
