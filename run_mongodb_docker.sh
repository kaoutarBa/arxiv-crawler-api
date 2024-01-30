#!/bin/bash

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

#give execute permissions to the script
#chmod +x run_mongodb.sh

#to run this script
#./run_mongodb.sh


#http://localhost:27017