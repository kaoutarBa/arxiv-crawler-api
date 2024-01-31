from flask import Flask, request, jsonify, send_file, make_response
from pymongo import MongoClient
from dotenv import load_dotenv
from src.metadata_crawler import crawler
import os

# Load environment variables from .env
load_dotenv()

# MongoDB configuration
MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DB_NAME")
COLLECTION_NAME = os.getenv("COLLECTION_NAME")

# MongoDB connection
client = MongoClient(MONGO_URI)
db = client.get_database(DB_NAME)
entries_collection = db.get_collection(COLLECTION_NAME)

# Create Flask app instance
app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

# Perform metadata crawling
crawler()


# Route to upload a new article
@app.route('/articles', methods=['POST'])
def upload_article():
    try:
        # Extract data from the request
        data = request.json

        # Validate that the required fields are present
        required_fields = ['id', 'title', 'authors', 'categories', 'links', 'published', 'summary', 'updated']
        if not all(field in data for field in required_fields):
            return jsonify({'error': 'Missing required fields'}), 400

        # Insert the metadata into the MongoDB collection
        entries_collection.update_one(
            {'id': data['id']},
            {'$set': data},
            upsert=True
        )

        return jsonify({'id': data['id']}), 201  # Respond with the document ID
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/articles', methods=['GET'])
@app.route('/articles/', methods=['GET'])
def list_articles():
    try:
        # Définir la page par défaut et le nombre d'articles par page
        #/articles?page=1&per_page=10
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 5))

        # Calculer l'indice de départ pour la pagination
        start_index = (page - 1) * per_page

        # Fetch les articles de la MongoDB collection avec pagination
        articles = list(entries_collection.find({}, {'_id': 0}).skip(start_index).limit(per_page))

        return jsonify({'articles': articles}),200, {'Content-Type': 'application/json; charset=utf-8'}

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to describe a specific article
@app.route('/articles/<id>', methods=['GET'])
def describe_article(id):
    try:
        # Fetch the article with the given ID from the MongoDB collection
        article = entries_collection.find_one({'id': id}, {'_id': 0})

        if article:
            return jsonify({'article': article})
        else:
            return jsonify({'error': 'Article not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/text/<id>.txt', methods=['GET'])
def get_article_summary(id):
    try:
        # Recherche de l'article dans la base de données
        article = entries_collection.find_one({'id': id}, {'_id': 0, 'summary': 1})

        if article:
            # Création d'un fichier texte temporaire pour le résumé
            temp_file_path = f'{id}_summary.txt'
            with open(temp_file_path, 'w') as temp_file:
                temp_file.write(article['summary'])

            # Envoi du fichier en réponse
            return send_file(temp_file_path, as_attachment=True)
        else:
            return jsonify({'error': f'Article with ID {id} not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        # Suppression du fichier texte temporaire après l'envoi
        if temp_file_path and os.path.exists(temp_file_path):
            os.remove(temp_file_path)

@app.route('/', methods=['GET'])
def handle_welcome():
    title = "Welcome !"
    message = "Enjoy interacting with the API in order to get metadata of articles from Arxiv !"

    content = f"<html><head><title>{title}</title></head><body><h1>{title}</h1><p>{message}</p></body></html>"
    response = make_response(content)
    return response

@app.errorhandler(404)
def page_not_found(error):
    title  = "Oups !"
    message = "Apparently, there is an error when trying to retrieve the request data!<br/> Make sure to issue a correct query.<br/> Read the Manual for guidance."
    content = f"<html><head><title>{title}</title></head><body><h1>{title}</h1><p>{message}</p></body></html>"
    response = make_response(content)
    return response


if __name__ == '__main__':
    app.run(debug=True)
