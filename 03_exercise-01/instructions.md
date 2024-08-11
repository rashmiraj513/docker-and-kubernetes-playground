# Instructions

1. Dockerize the app.

2. Create appropriate image.

   > HINT: Have a brief look at the app code to configure your images correctly!

3. Launch a container for the created image, making sure,
   that the app inside the container works correctly and is usable.
4. Re-create the container and assign name to the container.
   Use these names to stop and restart both containers.

5. Clean up (remove) all stopped (and running) container,
   clean up all created image.

6. Re-build the image - this time with name and tag assigned to them.

7. Run new container based on the re-built image, ensuring that the container is removed automatically when stopped.

# Solution:

1. Check the `Dockerfile` file.
2. Use the following command:

```bash
docker build .
```

3. Use the following command:

```bash
docker run -p 8080:3000 <docker_image_id>
```

4. Use the following command:

```bash
docker run -p 8080:3000 --name <container_name> <docker_image_id> # Create a new container with the name specified
docker stop <container_name> # Stop the container
docker start <container_name> # Start the container
```

5. Use the following command:

- To remove the containers:

```bash
# Stop all the running containers first and then remove all the container
docker container prune # 1st way - This will remove all the stopped containers.
docker rm <container_1> <container_2> ... # 2nd way - This is the second way of removing all the container by specifying their name by space-separated values.
```

- To remove the images:

```bash
docker image prune # 1st way - This will remove all the images that has no container attached to it.
docker image prune -a # 2nd way- This will remove all the images that has at least one container attached to it.
docker rmi <image_id_1> <image_id_2> ... # 3rd way - This is the second way of removing all the images by specifying their id by space-separated values.
```

6. Use the following command:

```bash
docker build -t <image_tag> .
```

7. Use the following command:

```bash
docker run -p 8080:3000 -d --name <container_name> --rm <image_tag>
```
