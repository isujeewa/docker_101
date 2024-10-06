# Use Alpine as the base image
FROM alpine:latest

# Set the working directory inside the container
WORKDIR /usr/share/nginx/html

# Copy the HTML file from the local 'source' directory to the container's /usr/share/nginx/html directory
COPY source/index.html .

# Verify the copied file by using cat to display it (just for demonstration)
CMD ["cat", "/usr/share/nginx/html/index.html"]
