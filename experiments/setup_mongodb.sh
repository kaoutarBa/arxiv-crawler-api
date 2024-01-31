#!/bin/bash

#on windows, i used WSL 2 terminal aside with Powershell Extension on Vscode
# This script is run on WSL
#it is recommended to activate the WSL integration in Docker Desktop settings (Windows).

#give execute permissions to the script
#chmod +x run_mongodb.sh

#to run this script
#./setup_mongodb.sh


#http://localhost:27017


# Pull MongoDB Docker Image
docker pull mongo

# Run MongoDB Container
docker run -d -p 27017:27017 --name my-mongodb mongo

# Access MongoDB Container (Optional)
# docker exec -it my-mongodb mongo

# Provide instructions or additional commands if needed
echo "MongoDB container is running. Use 'docker exec -it my-mongodb mongo' to access the MongoDB shell."

# To stop and remove the container (Optional)
# docker stop my-mongodb
# docker rm my-mongodb
