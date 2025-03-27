import os

# Define Project Folder Structure
folders = [
    "translation_project",
    "translation_project/src",
    "translation_project/data",
    "translation_project/models",
    "translation_project/logs"
]

files = [
    "translation_project/requirements.txt",
    "translation_project/app.py",
    "translation_project/train.py",
    "translation_project/evaluate.py",
    "translation_project/api.py",
    "translation_project/src/__init__.py",
    "translation_project/src/data_loader.py",
    "translation_project/src/model.py",
    "translation_project/src/utils.py"
]

# Create folders
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Create files
for file_path in files:
    with open(file_path, "w") as f:
        pass

print("Project structure created successfully!")
