import requests
import sqlite3
import feedparser

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

    metadata['links'] = [{'rel': link.rel, 'title': link.title if hasattr(link, 'title') else '', 'href': link.href} for link in entry.links]

    return metadata

def save_to_database(metadata_list):
    conn = sqlite3.connect('arxiv_database.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS arxiv_entries (
            id TEXT PRIMARY KEY,
            title TEXT,
            published TEXT,
            updated TEXT,
            summary TEXT,
            authors TEXT,
            categories TEXT,
            links TEXT
        )
    ''')

    for metadata in metadata_list:
        cursor.execute('''
            INSERT OR IGNORE INTO arxiv_entries (id, title, published, updated, summary, authors, categories, links)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (metadata['id'], metadata['title'], metadata['published'], metadata['updated'], metadata['summary'],
              str(metadata['authors']), str(metadata['categories']), str(metadata['links'])))

    conn.commit()
    conn.close()

def main():
    start_index = 0
    max_results = 100

    arxiv_entries = fetch_arxiv_data(start_index, max_results)

    if arxiv_entries:
        metadata_list = [extract_metadata(entry) for entry in arxiv_entries]
        save_to_database(metadata_list)
        print(f"Metadata for {len(metadata_list)} entries saved to the database.")

if __name__ == "__main__":
    main()
