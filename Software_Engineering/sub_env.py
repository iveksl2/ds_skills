import os
import subprocess

my_env = os.eniron().copy()
my_env["PATH"] = os.pathsetp.join(["/opt/myapp/", my_env["PATH"]])

result = subprocess.run(['myapp'], env=my_env)

# https://docs.python.org/3/library/subprocess.html
