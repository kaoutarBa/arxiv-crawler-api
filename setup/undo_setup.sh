#!/bin/bash

# Désactiver l'environnement virtuel
echo "Deactivating virtual environment..."
source deactivate
echo "Virtual environment deactivated."
# Supprimer l'environnement virtuel
echo "Removing virtual environment..."
rm -r venv/
echo "Virtual environment removed"

# Supprimer l'environnement virtuel
echo "Stopping my-mongodb ..."
docker stop my-mongodb
echo "my-mongodb is stopped"

#remove the container
echo "Removing my-mongodb ..."
docker rm my-mongodb
echo "my-mongodb is removed"

