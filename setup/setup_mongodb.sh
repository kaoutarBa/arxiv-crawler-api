#!/bin/bash

# Pull MongoDB Docker Image
docker pull mongo

# Run MongoDB Container
docker run -d -p 27017:27017 --name my-mongodb mongo


echo "MongoDB container is running"


