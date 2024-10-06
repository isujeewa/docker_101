# Use Alpine as the base image
FROM alpine:latest

# Set the working directory inside the container
WORKDIR /usr/share/nginx/html

# Add the HTML file from the local 'source' directory to the container's /usr/share/nginx/html directory
ADD source/index.html .

# Fetch a remote file and add it to the same directory
ADD https://example.com/remote.html /usr/share/nginx/html/remote.html

# Verify the copied and fetched files by using cat to display both (just for demonstration)
CMD ["sh", "-c", "cat /usr/share/nginx/html/index.html /usr/share/nginx/html/remote.html"]
