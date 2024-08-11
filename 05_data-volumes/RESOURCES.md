# Notes of Section 02

## Docker Volume

- To list the anonymous volume, use the following command: `docker volume ls`.
- To remove the volumne, use the following command: `docker volume rm <volume_name_1> <volume_name_2>` or, `docker volume prune`.
- If we want to create named volume then we need to specify this at the time of running the container. To do this, use the following command: `docker run -d -p 3000:3000 --name <container_name> -v <volume_local_folder:volume_docker_folder>  <image_name>`.

### Bind Mounts

- A Docker bind mount is a direct connection between a file or directory on the host computer and a directory within a container.
- Bind mounts are stored on the host machine where Docker is running and can be useful for: Saving data between runs, Stateful applications, Communicating files and directories between the host and the container, and Mounting source code into the container.
- For implementing bind mount, use the following command:

```bash
docker run -d --rm -p 3000:3000 --name feedback-app -v feedback:/app/feedback -v "<absolute_path_of_your_folder":/app" -v /app/node_modules <image_name>
```

# Arguments and Environments

- You can also pass the value from environment files using `.env` using `--env-file ./.env`.
- You can also pass different arguments using `--build-args`.

- (`-v /app/node_modules` is anonymous volume which is written because of `/node_modules` of container is getting overwritten to the local folder).
- For shortcut in windows, use the following command: `-v "%cd%":/app`.
- Here, you can also specify that the bind mount is for read-only using the following command:

```bash
docker run -d --rm -p 3000:3000 --name feedback-app -v feedback:/app/feedback -v "<absolute_path_of_your_folder":/app:ro" -v /app/node_modules <image_name>
```

> **Note:** The anonymous volumes are removed automatically when a container is removed. This happens when you start/run a container with the `--rm` option. If you start a container without that option, the anonymous volume would not be removed, even if you remove the container (with `docker rm ...` command). Still, if you then re-create and re-run the container i.e., you run `docker run ...` again, a new anonymous volume will be created. So even though the anonymous volume wasn't removed automatically, it'll also not be helpful because a different anonymous volume is attached the next time the container starts (i.e., you removed the old container and run a new one). Now, you just start piling up a bunch of unused anonymous volumes - which can be cleared using the above mentioned commands.
