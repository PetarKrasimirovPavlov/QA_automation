import os
import subprocess

# get environment as user input or use default
env = input("Enter environment URL (or press Enter for default): ").strip()
if not env:
    env = "https://reqres.in/"

# Set env as environment variable
env_vars = os.environ.copy()
env_vars["BASE_URL"] = env

cmd = ["pytest",
       "-s",
       ]

subprocess.run(cmd, env=env_vars)