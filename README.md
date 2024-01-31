# arxiv-crawler-api
ArXiv Crawler Flask API developed as part of practical training for the 'Python for Data Intensive Applications' course at MS SIO, CentraleSupélec.

### Clone the repository locally
From Git
```
git clone https://github.com/kaoutarBa/arxiv-crawler-api.git
```
From GitLab
```
git clone https://github.com/kaoutarBa/arxiv-crawler-api.git
```

### Description
a crawler that extracts metadata from ArXiv.org and stores them in a Flask application through an API. The API can be used to query the collection of articles to power the next phase of the project 

## How to run the application locally
Make sure to have Docker installed & MongoDB, it's for setting up a mongoDB server on a docker container
I used Vscode for the development process, under Windows, so I used Powershell Extension as a Terminal
for more details about setting up a virtual environnement
Make sure to have Python 3.12.1
```
python --version
```


### Setting Up Virtual environement Venv
Install venv
```
python -m venv venv
```
Activate the virtual environment using the command:
```
venv\Scripts\Activate.ps1
```
If you want to deactivate it run 
```
If you want to deactivate this virtual environment execute :
```
Install dependencies
```
pip install -r requirements.txt
```
If you want to delete the virtual environment execute
```
rm -r venv/
```
#### Setting up MongoDB on Docker Container
```
docker-compose up -d
```

#### test

### Run the Flask API
It will be running on http://127.0.0.1:5000
```
$env:FLASK_APP="src.app"
flask run
```
#### interact with the API
