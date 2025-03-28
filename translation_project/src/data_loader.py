
# Data ingestion and Preprocessing
import os
import json
from datasets import Dataset
from src.data_collector import data_collection
# load the JSON data 
def load_data(file_path):

    if not os.path.exists(file_path):
        print(f"{file_path} not found running data collection pipeline")
        data_collection()

    with open(file_path,'r',encoding="utf-8") as f:
        data = json.load(f)
    return data

def preprocess_data(data):
    # convert data into HuggingFace Dataset format
    return Dataset.from_dict({
        "input_text":[item["input_text"] for item in data],
        "target_text":[item["target_text"] for item in data]

    })

def get_dataset(train_path="data/train_data.json",val_path = "data/val_data.json"):
    train_data = preprocess_data(load_data(train_path))
    val_data =preprocess_data(load_data(val_path))
    return train_data, val_data


