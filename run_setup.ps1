echo "Setting up ..."
# Exécuter le script de configuration de MongoDB
echo "Running MongoDB setup script..."
.\setup_mongodb.ps1
echo "MongoDB setup complete."

# Créer l'environnement virtuel
echo "Creating virtual environment..."
python -m venv venv
echo "Virtual environment created."

# Activer l'environnement virtuel (sous Windows)
echo "Activating virtual environment..."
.\venv\Scripts\Activate.ps1
echo "Virtual environment activated."

# Installer les dépendances
echo "Installing dependencies..."
pip install -r requirements.txt
echo "Dependencies installed."

# Définir la variable d'environnement FLASK_APP
echo "Setting FLASK_APP environment variable..."
$env:FLASK_APP="src.app"
echo "FLASK_APP environment variable set."

# Exécuter l'application Flask
echo "Running Flask application..."
flask run
