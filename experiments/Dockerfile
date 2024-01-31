# Dockerfile for crawler container

# Utiliser une image Python officielle en tant qu'image de base
FROM python:3.8

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier le fichier requirements.txt dans le conteneur
COPY requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste des fichiers dans le conteneur
COPY . .

# Commande par défaut à exécuter lors du démarrage du conteneur
CMD ["python", "arxiv_metadata_crawler.py"]
