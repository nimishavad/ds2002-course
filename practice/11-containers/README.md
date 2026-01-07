## Running Containers

### Pulling Container Images

To pull a container image, find its location from Docker Hub or another registry. This should appear
something like:

```
docker pull ghcr.io/ds3002/course:latest
```

To view all the containers you have pulled to your computer,

```
docker images
```

To delete an image, use the `rmi` remove image command with either the container name:tag or ID.

```
docker rmi image_name
```

To delete all unused images:

```
docker system prune
```

## Running in Detached Mode

To run a container in detached mode, append the `-d` flag to the `docker run` command with the
container image name:

```
docker run -d nginx
```

## Running in Interactive Mode

To work with a container interactively, append the `-it` flag to the `docker run` command with
the container image name. Be sure to add a shell or some other executable program after the image
name:

```
docker run -it ubuntu /bin/bash
```

## View Running Containers

To see all containers running locally:

```
docker ps
```

Should give some results like this:

```
CONTAINER ID   IMAGE                          COMMAND       CREATED          STATUS          PORTS     NAMES
2ad2502e9600   ghcr.io/ds3002/course:latest   "/bin/bash"   36 minutes ago   Up 36 minutes             epic_hodgkin
```

You can now refer to any specific container by using either the FULL name `epic_hodgkin`, or the first few characters
of the Container ID, such as `2ad2`

## Stop a Running Container

To stop a container

```
docker stop epic_hodgkin
```

or

```
docker stop 21d2
```

### Add an Environment Variable

To inject ENV variables into a container, add the `-e` flag with a Key-Value mapping when you run the container:

```
docker run -it -e MYKEY=myvalue ubuntu:latest /bin/bash
```

## Attach a Local Port

To map a local port from a container to your workstation, use the `-p` flag with a mapping of
`HOST_PORT:CONTAINER_PORT`. This allows you to view/test a service listening on that port:

```
docker run -d -p 8080:80 nginx
```

## Mount Storage

To mount a directory from your local workstation into a container when launched, use the `-v` flag with
a mapping of `HOST_VOLUME:CONTAINER_VOLUME`:

```
docker run -it -v /home/user/project:/root/project ubuntu:latest /bin/bash
```

### Inspect Properties of a Container

To inspect all metadata attributes about a running container, such as IP address, or volume mounts, etc.
use the `inspect` command. This will return a JSON payload of fields:

```
docker inspect 2ad2
```

## Review Logs

To view the output logs from a running container:

```
docker logs 2ad2
```

### Shell into a Running Container

Finally, to "hop" into a running container that is running in detached mode, use the `exec -it` command
against the ID or name of the running container. Be sure to add a shell or other executable after the name
of the container.

```
docker exec -it 2ad2 /bin/bash
```

## Apptainer - Containers in HPC Environments



## Creating Containers

This directory contains a few container examples developed for the Data Engineering course. We focus on the mechanism of the build process rather than the specific implementation details underlying each project.

### `whalesay`

This is a famous demo container created by Docker to demonstrate an interactive
container image that takes input from a user. To build it, cd into this directory:

```
docker build -t whalesay .
```
To run it, simply append a command or quote or joke at the end of the `run` command:
```
docker run whalesay Hello everyone!
```

## `convert`

This is a simple Python ETL pipeline. You can build
it locally by changing into its directory and running:

```
docker build -t converter .
```
To try running it on your own, just map a directory to the `/data` path of the container and pass the
fictional ID `0987654321` as a parameter:

```
docker run -v ${PWD}:/data converter -i 0987654321
```

## Advanced Concepts

### Multi-Stage Builds

Multi-stage builds allow you to use multiple `FROM` statements in a Dockerfile, which helps create smaller final images by separating build dependencies from runtime dependencies:

```dockerfile
# Build stage
FROM python:3.11-slim as builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --user -r requirements.txt

# Runtime stage
FROM python:3.11-slim
WORKDIR /app
COPY --from=builder /root/.local /root/.local
COPY . .
ENV PATH=/root/.local/bin:$PATH
CMD ["python", "app.py"]
```

### Docker Compose

Docker Compose allows you to define and run multi-container Docker applications using a YAML file. This is useful for orchestrating services that need to work together:

```yaml
version: '3.8'
services:
  web:
    build: .
    ports:
      - "5000:5000"
  redis:
    image: redis:alpine
    ports:
      - "6379:6379"
```

Note the `build: .` statement for the `web` service. The `.` refers to the current directory and it is assumed that it contains a `Dockerfile` with the image build instructions. In contrast, the `redis` service will utilize an existing image `redis:alpine` from a public repository.

Run with: `docker-compose up`


### Dockerfile Best Practices

- Use specific version tags instead of `latest`
- Order Dockerfile instructions from least to most frequently changing
- Use `.dockerignore` to exclude unnecessary files
- Minimize the number of layers
- Use multi-stage builds for smaller images
- Run containers as non-root users when possible

### Container Orchestration

For production environments, consider container orchestration platforms:
- **Kubernetes**: Industry-standard for container orchestration
- **Docker Swarm**: Built-in orchestration for Docker
- **Amazon ECS**: AWS container orchestration service
- **Azure Container Instances**: Serverless containers on Azure

## Resources

* [What is a Container?](https://www.docker.com/resources/what-container/) - Introduction to containerization concepts
* [Docker Getting Started Tutorial](https://docs.docker.com/get-started/) - Official getting started guide
* [Docker Curriculum](https://docker-curriculum.com/) - Free interactive Docker tutorial
* [Play with Docker](https://labs.play-with-docker.com/) - Interactive Docker playground
* [Docker Official Samples](https://github.com/docker/awesome-compose) - Official Docker Compose examples
* [Docker Security Best Practices](https://docs.docker.com/engine/security/) - Security guidelines

### Container Registries

* [Docker Hub](https://hub.docker.com/) - Default public registry
* [GitHub Container Registry (GHCR)](https://github.com/features/packages) - Integrated with GitHub
* [Amazon ECR](https://aws.amazon.com/ecr/) - AWS container registry
* [Google Container Registry](https://cloud.google.com/container-registry) - GCP container registry
* [Azure Container Registry](https://azure.microsoft.com/services/container-registry/) - Azure container registry
