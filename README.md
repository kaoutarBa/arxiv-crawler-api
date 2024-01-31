# arxiv-crawler-api
ArXiv Crawler Flask API developed as part of practical training for the 'Python for Data Intensive Applications' course at MS SIO @CentraleSupélec.
### Description
a crawler that extracts metadata from ArXiv.org and stores them in a Flask application through an API, with relying on the [Arxiv API](https://info.arxiv.org/help/api/index.html).
The API can be used to query the collection of articles to power the next phase of the project Fil rouge, still in process

## Clone the repository locally
- From Github
```
git clone https://github.com/kaoutarBa/arxiv-crawler-api.git
```
- From GitLab
```
git clone https://github.com/kaoutarBa/arxiv-crawler-api.git
```

## How to run the application locally
Make sure to have Docker installed & MongoDB, it's for setting up a mongoDB server on a docker container
I used Vscode for the development process, on Windows, so I used Powershell Extension as a Terminal, also WSL2.
for more details about [setting up a virtual environnement in Vscode](https://medium.com/@dipan.saha/managing-git-repositories-with-vscode-setting-up-a-virtual-environment-62980b9e8106)

Make sure to have Python 3.12.1
```
python --version
```

On Windows/WSL2 or on Linux, make sure to install python3.10-venv
```
sudo apt install python3.10-venv
```
### Setting Up
In order to set up the virtual environnement, install the requirements, run the flask app
- On Windows/Powershell execute: 
```
.\setup\run_setup.ps1
```
- On Windows/WSL2 or on Linux, execute:
```
./setup/run_setup.sh
```
It will be running on http://127.0.0.1:5000

### Undo the set up
- On Windows/Powershell execute: 
```
.\setup\undo_setup.ps1
```
- On Windows/WSL2 or on Linux, execute:
```
./setup/undo_setup.sh
```
to run falsk app separately without redo the set up:
```
flask run
```
### Run tests

## Interact with API

Welcome Page (try it on the browser):
```
curl http://127.0.0.1:5000
```

##### Nonexistent Route
In case the route doesn't exist, it will render a message indicating the necessity of providing a valid request:
```
curl http://127.0.0.1:5000/nonexistent_route
```
##### Articles
To get articles:

```
curl "http://127.0.0.1:5000/articles"
```
You can specify also the page and the number of results by page:

```
curl "http://127.0.0.1:5000/articles?page=<page>&per_page=<per_page>"
```
It will render default page 1, and 10 results by page

##### Filter Articles based on their properties
List the first page with 5 articles.
```
curl "http://127.0.0.1:5000/articles?page=1&per_page=5"
```
List articles in the "math.GN" category.
```
curl "http://127.0.0.1:5000/articles?category=math.GN"
```
filter by author
```
curl "http://127.0.0.1:5000/articles?authors=Joud Khoury"
```
##### Upload an article 
Replace article_data with your actual JSON data:
- on WSL / Linux:
```
curl -X POST -H "Content-Type: application/json" -d '<article_data>' http://127.0.0.1:5000/articles
```
- An example on WSL / Linux:
```
curl -X POST -H "Content-Type: application/json" -d '{
  "id": "1234.5678v1",
  "title": "Sample Title",
  "authors": ["John Doe", "Jane Smith"],
  "categories": ["cs.AI"],
  "links": [
    {"rel": "alternate", "href": "http://arxiv.org/abs/1234.5678v1"},
    {"rel": "related", "title": "pdf", "href": "http://arxiv.org/pdf/1234.5678v1"}
  ],
  "published": "2024-01-31T12:00:00Z",
  "summary": "This is a sample article summary.",
  "updated": "2024-01-31T12:00:00Z"
}' http://127.0.0.1:5000/articles

```
- On Windows : 
```
Invoke-RestMethod -Uri 'http://127.0.0.1:5000/articles' -Method POST -Headers @{'Content-Type'='application/json'} -Body '<article_data>'

```
- An example on Windows :
```
Invoke-RestMethod -Uri 'http://127.0.0.1:5000/articles' -Method POST -Headers @{'Content-Type'='application/json'} -Body '{
  "id": "id000fortest",
  "title": "Sample Title",
  "authors": ["John Doe", "Jane Smith"],
  "categories": ["cs.AI"],
  "links": [
    {"rel": "alternate", "href": "http://arxiv.org/abs/id000fortest"},
    {"rel": "related", "title": "pdf", "href": "http://arxiv.org/pdf/id000fortest"}
  ],
  "published": "2024-01-31T12:00:00Z",
  "summary": "This is a sample article summary.",
  "updated": "2024-01-31T12:00:00Z"
}'
```


##### Get a specific Article
For example id="1911.11405v1"
```
curl "http://127.0.0.1:5000/articles/1911.11405v1"
```
##### Get Summary of a Specific Article
```
curl "http://127.0.0.1:5000/summary/1911.11405v1"
```
