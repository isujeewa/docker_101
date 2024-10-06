docker build -f Dockerfile.prod -t myapp-prod .

docker run -p 5122:5122 myapp-prod
