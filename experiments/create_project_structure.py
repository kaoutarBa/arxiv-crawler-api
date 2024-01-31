import os

# List of directories and files to create
project_structure = [
    'arxiv_crawler.py',
    'app.py',
    'tests/',
    'tests/test_arxiv_crawler.py',
    'venv/',
    'requirements.txt',
    '.git/',
    '.gitignore',
    'README.md',
]

# Create directories and files
for item in project_structure:
    full_path = os.path.join(os.getcwd(), item)
    if not os.path.exists(full_path):
        if '.' in item:
            with open(full_path, 'w'):
                pass
        else:
            os.makedirs(full_path)

print("Project structure created successfully!")
