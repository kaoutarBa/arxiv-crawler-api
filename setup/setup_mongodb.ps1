# Pull MongoDB Docker Image
echo "Pulling MongoDB Docker Image ..."
docker pull mongo
echo "MongoDB Docker Image is pulled"

# Run MongoDB Container
echo "Rnning MongoDB Docker Image ..."
docker run -d -p 27017:27017 --name my-mongodb mongo
echo "MongoDB container is running"

# To stop and remove the container (Optional)
# docker stop my-mongodb
# docker rm my-mongodb
