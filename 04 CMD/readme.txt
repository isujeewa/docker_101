The CMD instruction specifies the default command to run when the container starts. Let's create a Dockerfile that uses CMD to print a message.

docker build -t alpine-cmd-demo .
docker run alpine-cmd-demo
