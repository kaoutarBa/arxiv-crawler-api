#!/bin/bash

echo "Setting up ..."
# Exécuter le script de configuration de MongoDB
echo "Running MongoDB setup script..."
chmod +x setup_mongodb.sh
./setup_mongodb.sh
echo "MongoDB setup complete."

# Créer l'environnement virtuel
echo "Creating virtual environment..."
python3 -m venv venv
echo "Virtual environment created."

# Activer l'environnement virtuel (sous Linux)
echo "Activating virtual environment..."
source venv/bin/activate
echo "Virtual environment activated."

# Installer les dépendances
echo "Installing dependencies..."
pip install -r requirements.txt
echo "Dependencies installed."

# Définir la variable d'environnement FLASK_APP
echo "Setting FLASK_APP environment variable..."
export FLASK_APP=src.app
echo "FLASK_APP environment variable set."

# Exécuter l'application Flask
echo "Running Flask application..."
flask run
