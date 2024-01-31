'''import urllib, urllib.request
url = 'http://export.arxiv.org/api/query?search_query=all&start=1&max_results=1'
data = urllib.request.urlopen(url)
print(data.read().decode('utf-8'))'''


'''import urllib.request

url = 'http://export.arxiv.org/api/query?search_query=all'

# Open the URL and read the data
with urllib.request.urlopen(url) as response:
    arxiv_data = response.read().decode('utf-8')

# Specify the file name where you want to save the data
output_file_path = 'arxiv_response.xml'

# Write the data to the file
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    output_file.write(arxiv_data)

print(f"ArXiv API response saved to {output_file_path}")'''

import requests
import sqlite3
import feedparser

# Function to fetch and parse ArXiv API response using feedparser
def fetch_arxiv_data(start_index, max_results):
    base_url = 'http://export.arxiv.org/api/query'
    params = {
        'search_query': 'all',
        'start': start_index,
        'max_results': max_results
    }

    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        arxiv_data = response.text
        feed = feedparser.parse(arxiv_data)
        return feed.entries
    else:
        print(f"Error fetching data. Status Code: {response.status_code}")
        return None

# Function to extract metadata from ArXiv entry using feedparser
def extract_metadata(entry):
    metadata = {}
    metadata['title'] = entry.title.strip()
    metadata['id'] = entry.id.split('/')[-1].strip()
    metadata['published'] = entry.published.strip()
    metadata['updated'] = entry.updated.strip()
    metadata['summary'] = entry.summary.strip()

    # Additional metadata extraction can be added as needed

    return metadata

# Function to save metadata to SQLite database
def save_to_database(metadata_list):
    conn = sqlite3.connect('arxiv_database.db')
    cursor = conn.cursor()

    # Create a table if not exists
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS arxiv_entries (
            id TEXT PRIMARY KEY,
            title TEXT,
            published TEXT,
            updated TEXT,
            summary TEXT
        )
    ''')

    # Insert metadata into the database
    for metadata in metadata_list:
        cursor.execute('''
            INSERT OR IGNORE INTO arxiv_entries (id, title, published, updated, summary)
            VALUES (?, ?, ?, ?, ?)
        ''', (metadata['id'], metadata['title'], metadata['published'], metadata['updated'], metadata['summary']))

    # Commit changes and close the connection
    conn.commit()
    conn.close()

# Main function to iterate over ArXiv documents, extract metadata, and save to the database
def main():
    start_index = 0
    max_results = 10  # You can adjust this based on your needs

    arxiv_entries = fetch_arxiv_data(start_index, max_results)

    if arxiv_entries:
        metadata_list = [extract_metadata(entry) for entry in arxiv_entries]

        save_to_database(metadata_list)
        print(f"Metadata for {len(metadata_list)} entries saved to the database.")

if __name__ == "__main__":
    main()



