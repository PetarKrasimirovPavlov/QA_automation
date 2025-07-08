import os
import subprocess
from datetime import datetime

# get environment as user input or use default
env = input("Enter environment URL (or press Enter for default): ").strip()
if not env:
    env = "https://www.saucedemo.com/"

# Creating timestamp report path
timestamp = datetime.now().strftime("%d%m%Y_%H%M%S")
report_path = f"report_{timestamp}.html"

# Set env as environment variable
env_vars = os.environ.copy()
env_vars["BASE_URL"] = env

cmd = ["pytest",
       "-n", "3",
       f"--html=reports/{report_path}",
       "--self-contained-html"
       ]

subprocess.run(cmd, env=env_vars)
print(f"Report saved to: {report_path}")