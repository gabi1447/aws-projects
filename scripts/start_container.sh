#!/bin/bash

# Pull the Docker image from docker hub 

docker pull gabi1447/aws-code-build-python-flask:latest

# Run the Docker image as a container

docker run -d --name python-flask -p 5000:5000 gabi1447/aws-code-build-python-flask:latest 