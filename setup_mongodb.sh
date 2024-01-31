#!/bin/bash

#on windows, i used WSL 2 terminal aside with Powershell Extension on Vscode
# This script is run on WSL
#it is recommended to activate the WSL integration in Docker Desktop settings (Windows).

#give execute permissions to the script
#on WSL /
#chmod +x setup_mongodb.sh

#to run this script
#./setup_mongodb.sh


#http://localhost:27017


# Pull MongoDB Docker Image
docker pull mongo

# Run MongoDB Container
docker run -d -p 27017:27017 --name my-mongodb mongo


echo "MongoDB container is running"

# To stop and remove the container (Optional)
# docker stop my-mongodb
# docker rm my-mongodb
