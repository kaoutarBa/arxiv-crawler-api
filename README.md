# arxiv-crawler-api
ArXiv Crawler Flask API developed as part of practical training for the 'Python for Data Intensive Applications' course at MS SIO @CentraleSupélec.
### Description
a crawler that extracts metadata from ArXiv.org and stores them in a Flask application through an API. The API can be used to query the collection of articles to power the next phase of the project 
### Clone the repository locally
From Github
```
git clone https://github.com/kaoutarBa/arxiv-crawler-api.git
```
From GitLab
```
git clone https://github.com/kaoutarBa/arxiv-crawler-api.git
```

## How to run the application locally
Make sure to have Docker installed & MongoDB, it's for setting up a mongoDB server on a docker container
I used Vscode for the development process, on Windows, so I used Powershell Extension as a Terminal, also WSL2.
for more details about setting up a virtual environnement : LINK

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
### Run tests

### Interact with API
