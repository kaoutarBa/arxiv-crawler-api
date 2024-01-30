import requests
import feedparser
from pymongo import MongoClient

def fetch_arxiv_data(start_index, max_results):
    base_url = 'http://export.arxiv.org/api/query'
    params = {
        'search_query': 'all',
        'start': start_index,
        'max_results': max_results
    }

    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        arxiv_feed = feedparser.parse(response.text)
        return arxiv_feed.entries
    else:
        print(f"Error fetching data. Status Code: {response.status_code}")
        return None

def extract_metadata(entry):
    metadata = {}

    metadata['title'] = entry.title
    metadata['id'] = entry.id.split('/')[-1]
    metadata['published'] = entry.published
    metadata['updated'] = entry.updated

    metadata['summary'] = entry.summary

    # Extracting all authors
    metadata['authors'] = [author.name for author in entry.authors]

    metadata['categories'] = [category.term for category in entry.tags]

    metadata['links'] = [{'rel': link.rel, 'title': link.title, 'href': link.href} if hasattr(link, 'title') else {'rel': link.rel, 'href': link.href} for link in entry.links]

    return metadata

def save_to_database(metadata_list):
    client = MongoClient('mongodb://localhost:27017/')
    db = client['arxiv_metadata_db']
    entries_collection = db['arxiv_metadata_entries']

    for metadata in metadata_list:
        entries_collection.update_one(
            {'id': metadata['id']},
            {'$set': metadata},
            upsert=True
        )

    print(f"Metadata for {len(metadata_list)} entries saved to MongoDB.")

def main():
    start_index = 0
    max_results = 20

    arxiv_entries = fetch_arxiv_data(start_index, max_results)

    if arxiv_entries:
        metadata_list = [extract_metadata(entry) for entry in arxiv_entries]
        save_to_database(metadata_list)

if __name__ == "__main__":
    main()
