# ROS Jupyter Notebook with ROS in Docker [![](https://img.shields.io/docker/pulls/frankjoshua/ros-jupyter)](https://hub.docker.com/r/frankjoshua/ros-jupyter) [![CI](https://github.com/frankjoshua/docker-ros-jupyter/workflows/CI/badge.svg)](https://github.com/frankjoshua/docker-ros-jupyter/actions)

## Description

Runs a Jupyter Notebook with ROS in a Docker container. Probably need --network="host" because ROS uses ephemeral ports.

## Example

```
docker run -it \
    -v "$PWD:/home/xplore/ros-jupyter" \
    -p 8888:8888 \
    ghcr.io/epflxplore/ros-course:latest
```

## Building

Use [build.sh](build.sh) to build the docker containers.

<br>Local builds are as follows:

```
./build.sh -t epflxplore/ros-course -l
```

## Testing

Github Actions expects the DOCKERHUB_USERNAME and DOCKERHUB_TOKEN variables to be set in your environment.

## License

Apache 2.0

## Author Information

Joshua Frank [@frankjoshua77](https://www.twitter.com/@frankjoshua77)
<br>
[http://roboticsascode.com](http://roboticsascode.com)
