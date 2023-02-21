This Dockerfile uses the python:3.9-alpine base image, which includes a Python interpreter. The COPY instruction copies the app.py script into the /app directory in the container, and the WORKDIR instruction sets the working directory to /app.

The CMD instruction specifies the command to run when the container starts. In this case, it runs the python interpreter and passes the app.py script as an argument.

When the container starts, the python interpreter will run the app.py script and display the message "Hello World from Docker!" on the console.
