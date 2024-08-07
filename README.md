# Docker Learning Repository

Welcome to my Docker Learning repository! This repository is dedicated to helping me learn and practice Docker. It contains a variety of
exercises, tutorial codes, and mini-projects designed to enhance my understanding of Docker.

## Topics

## Projects

## Notes

- **Images:** Read-only templates used to create containers. They contain the application code, libraries, dependencies, and any other files needed to run the application. Images are built from a set of instructions in a Dockerfile.
- **Containers:** Running instances of Docker images. They are lightweight, isolated environments that execute applications. Containers include the application and its dependencies, ensuring consistency across different environments.

> **Note:** In essence,
>
> - Images are the blueprint, and containers are the instances of that blueprint in action.
> - Images define what gets run, and containers are the actual running applications.
> - Always use double quotes inside `Dockerfile`.

### Command to build an image

- `docker build .`
- `docker run -p 3000:3000 <image>` - The first `3000` is the docker localhost whereas the second `3000` is the host's localhost.
- `docker stop <image_name>`
- `docker ps` - To see all the running containers.
- `docker ps -a` - To see all the previously running containers along with currently running containers.
- `docker run -it node` - Run the `node` image in interactive mode

### Dockerfile Components

- `FROM node`:
- `WORKDIR /app`:
- `COPY . /app`:
- `RUN npm install`:
- `EXPOSE 80`:
- `CMD ["node", "server.js"]`:
