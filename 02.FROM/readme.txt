The FROM statement pulls the base image.

# Step 1: Build the Docker image from the Dockerfile
docker build -t hello-container .   // Build an image named "hello-container" from the current directory

# Step 2: Run the container using the built image
docker run hello-container          // Run the "hello-container" image and execute the CMD instruction

# Optional: List all Docker images to see the newly created image
docker images                       // List all Docker images available locally

# Optional: View running containers to confirm the container executed
docker ps                           // List running containers (likely empty, as this container will terminate after execution)

# Optional: View all containers, including stopped ones, to see the output container after it runs
docker ps -a                        // List all containers, including stopped ones

# Optional: View the logs of the stopped container to see the output again
docker logs <container_id>          // View the logs of the container to see "Hello, I am a container!" message

# Optional: Remove the container after execution
docker rm <container_id>            // Remove the stopped container

# Optional: Remove the image if no longer needed
docker rmi hello-container          // Remove the "hello-container" image
