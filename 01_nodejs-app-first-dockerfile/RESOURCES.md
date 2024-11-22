# Notes of Section 01

- **Images:** Images are read-only templates, which can be used to create containers. They contain the application code, libraries, dependencies, and any other files needed to run the application. Images are built from a set of instructions in a Dockerfile.
- **Containers:** Running instances of Docker images. They are lightweight, isolated environments that execute applications. Containers include the application and its dependencies, ensuring consistency across different environments.

> **Note:** In essence,
>
> - Images are the blueprint, and containers are the instances of that blueprint in action.
> - Images define what gets run, and containers are the actual running applications.
> - Always use double quotes inside `Dockerfile`.

## Dockerfile Components

- `FROM node:18` - Uses the Node.js v18 image as the base for your application.
- `WORKDIR /app` - Sets the working directory inside the container to /app.
- `COPY . /app` - Copies your app's code into the container at /app.
- `RUN npm install` - Installs dependencies listed in package.json.
- `EXPOSE 80` - In the Dockerfile, this `EXPOSE` is optional. It documents that a process in the container will expose this port. But you still need to actually expose the port with `-p` when running `docker run` command. So, technically, `-p` is the only required part when it comes to listening on a port. Still, it is a best practice to also add `EXPOSE` in the `Dockerfile` to document this behavior.
- `CMD ["node", "server.js"]` - Runs server.js with Node.js when the container starts.

## Command to build an image and run it

- `docker build .`- Creates a Docker image.
- `docker run -p 3000:3000 <image>` - The first `3000` is the docker localhost (where you want to access the application) whereas the second `3000` is the host's localhost (which is exposed to container). However, `-p 3000:3000` is optional but if this flag is not provided then docker container will run but we won't be able to run the localhost. To run the container on the localhost, we need to specify this flag.
- `docker stop <image_name>` - Stops the docker image.
- `docker ps` - To see only the running containers.
- `docker ps -a` - To see all the previously running containers along with currently running containers.
- `docker run -it node` - Run the `node` image in interactive mode
- `docker start <container_name>` - Restarting an old container which exited earlier. With this command, the container keeps running in the background (Verify using `docker ps` command) and doesn't block the terminal like `docker run` command. This happens because of attached and detached mode. For `docker run` command, attached mode is default whereas for `docker start` command, detached mode is default.

  > - To run in detached mode, use `-d` flag like `docker run -p 3000:80 -d <docker_container>`
  > - If we want to attach again then use `docker attach <docker_container>`.
  > - To get logs, we can use `logs` like `docker logs <docker_container>` to get all the past logs. Also, we can use the flag `-f` to follow the future logs like `docker logs -f <docker_container>`. This is similar like running in attached mode.

## Command to remove a container or, image

- To remove one or more containers, use `docker rm <container_name_1> <container_name_2>...`
- To remove one or, more images, use `docker rmi <image_id_1> <image_id_2>...`
- To remove all images, use `docker image prune`.
- To remove stopped container automatically, use `docker run -p 3000:3000 -d --rm <docker_image>`. This command makes sure that whenever this container stops, it will be removed.

## Naming and Tagging for containers and images

- To provide a name for a container at the time of running, use the following command: `docker run -p 3000:80 -d --rm --name <container_name> <image_key>`
- Now, this <containe_name> can be used to stop, restart and do other things with the container.

- Name for images is also known as tags. The image tag consists of two parts: first one is `name` (also known as repository) and the second one is `tag`. The name is used to create a group of possible more specialized images whereas the tag defines a specialized image within a group of images.
  > - For e.g.: `node:14` where `node` is the name of the image, it represents a group of node images and 14 is the tag of the image which represents the version, and together both specifies 14th version of node.
  > - Use the following command: `docker build -t goals:latest`
  > - Here, the tag part is optional.

> **Note:** To list all the images, use `docker images` command. Also, we can't remove an image if that image is currently in use even by a closed container. Also, we can't remove a container that is currently running.

## Copying files into and from a container

- To copy files to a container from the local, use `docker cp <local_file_path_> <container_name:/directory_inside_container>`
  > - `docker cp test/hello.txt e6bf557f1b40:/test`
- To copy files from a container to local, use `docker cp <container_name:/directory_inside_container> <local_file_path>`
  > - `docker cp e6bf557f1b40:/test test/hello.txt`

## Renaming image tags

- To rename an image tag, we can use the following command:

```bash
docker tag <old_tag> <new_tag>
```

- Remember that after renaming the tag, the Docker will create a new image with the new tag and the image with old tag will remain as it is.

## Sharing docker images

- To share a docker image, you can push a docker image to the docker hub and then if the docker repository is public then anyone can pull this docker image and use this. If the docker repository is private then you can control who can pull this image.
- To push a docker image on docker hub, the tag of docker image should be the name of the docker hub repository and then you can use the following command `docker push <repository_name>`. Make sure that you are logged in the terminal.
- Once the `docker push` command is successful then you can pull this image in another devices and run this image.
- If you make any changes to the image and pushed the changes to repository then you need to pull again in another devices to make those changes visible.

> **Note:** If no CMD is specified, then the container will execute the base image commands. If no base image and no CMD then it will generate error.

> **Note:** For all docker commands, where an ID can be used, don't always copy/write out the full id. There you can use the first (few) character(s) - just enough to have a unique identifier. This applies to all Docker commands where IDs are needed.

> **Note:** For any change to reflect, we need to re-build the image and then run it so that code changes gets reflected using `COPY` command of Dockerfile.

> **Note:** Use `--help` to know more about some commands e.g., `docker --help`.

> **Note:** The flag `-i` is used only when you need to restart the container, i.e., the flag `-i` will be used only with `docker start` command (It is possible that you have to use `-a` flag in the context if you want the terminal to open in interactive as well as attached mode). But when you are running a new container then for interactivity, you need to use `-it` flag. Both flag is used for interactivity.
