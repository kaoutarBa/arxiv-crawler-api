import os

from dotenv import load_dotenv
from flask import Flask, jsonify, make_response, request, send_file
from pymongo import MongoClient

from src.metadata_crawler import crawler

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

# Perform metadata crawling
crawler()


# Route to upload a new article
@app.route("/articles", methods=["POST"])
def upload_article():
    try:
        # Extract data from the request
        data = request.json

        # Validate that the required fields are present
        required_fields = [
            "id",
            "title",
            "authors",
            "categories",
            "links",
            "published",
            "summary",
            "updated",
        ]
        if not all(field in data for field in required_fields):
            return jsonify({"error": "Missing required fields"}), 400

        # Insert the metadata into the MongoDB collection
        entries_collection.update_one({"id": data["id"]}, {"$set": data}, upsert=True)

        return jsonify({"id": data["id"]}), 201  # Respond with the document ID
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/articles/", methods=["GET"])
@app.route("/articles", methods=["GET"])
def list_articles():
    try:
        # Define default values for page and per_page
        page = int(request.args.get("page", 1))
        per_page = int(request.args.get("per_page", 10))

        # Calculate the starting index for pagination
        start_index = (page - 1) * per_page

        # Construct the query based on query parameters
        query = {}

        # Filter by category
        category = request.args.get("category")
        if category:
            query["categories"] = category

        # Filter by authors
        authors = request.args.get("authors")
        if authors:
            query["authors"] = authors
        # Fetch articles from the MongoDB collection with pagination and filters
        articles = list(
            entries_collection.find(query, {"_id": 0}).skip(start_index).limit(per_page)
        )

        return jsonify({"articles": articles}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Route to describe a specific article
@app.route("/articles/<id>", methods=["GET"])
def describe_article(id):
    try:
        # Fetch the article with the given ID from the MongoDB collection
        article = entries_collection.find_one({"id": id}, {"_id": 0})

        if article:
            return jsonify({"article": article})
        return jsonify({"error": "Article not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/summary/<id>", methods=["GET"])
def get_article_summary(id):
    try:
        # Fetch the article from the MongoDB collection
        article = entries_collection.find_one({"id": id}, {"_id": 0, "summary": 1})

        if article:
            # Return the summary as JSON response
            return jsonify({"summary": article["summary"]})
        return jsonify({"error": f"Article with ID {id} not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/", methods=["GET"])
def handle_welcome():
    title = "Welcome !"
    message = "Enjoy interacting with the API in order to get metadata of articles from Arxiv !"

    content = f"<html><head><title>{title}</title></head><body><h1>{title}</h1><p>{message}</p></body></html>"
    response = make_response(content)
    return response


@app.errorhandler(404)
def page_not_found(error):
    title = "Oups !"
    message = "Apparently, there is an error when trying to retrieve the request data!<br/> Make sure to issue a correct query.<br/> Read the Manual for guidance."
    content = f"<html><head><title>{title}</title></head><body><h1>{title}</h1><p>{message}</p></body></html>"
    response = make_response(content)
    return response


if __name__ == "__main__":
    app.run(debug=True)
