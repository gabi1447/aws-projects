#!/bin/bash

# stop and delete docker container if any

CONTAINER_ID=`docker ps | awk -f " " '{print $1}'`
docker rm -f $CONTAINER_ID
