import requests
import feedparser

def crawl_arxiv():
    arxiv_url = "https://export.arxiv.org/api/query?search_query=all:electron&start=0&max_results=1"

    response = requests.get(arxiv_url)
    feed = feedparser.parse(response.text)

    # Extract metadata and process as needed
    for entry in feed.entries:
        title = entry.title
        summary = entry.summary
        

        # Store metadata or do further processing
        print(f"Title: {title}\nSummary: {summary}\n")

if __name__ == "__main__":
    crawl_arxiv()
