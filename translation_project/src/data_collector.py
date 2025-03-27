
from datasets import load_dataset
import json
import random
import os

def fetch_translation_data(dataset_name="opus100",lang_pair=("en","es"),num_samples=5000):
    dataset= load_dataset(dataset_name,f"{lang_pair[0]}-{lang_pair[1]}",split="train")

    dataset = dataset.shuffle(seed=42).select(range(min(num_samples,len(dataset))))

    return [
        {"input_text": example[lang_pair[0]], "taget_text": example[lang_pair[1]]} for example in dataset
    ]

def save_data_to_json(data,file_path="./data/train_data.json"):
    os.makedirs(os.path.dirname(file_path),exist_ok=True)
    with open(file_path,'w',encoding="utf-8") as f:
        json.dump(data,f,ensure_ascii=False,indent=4)
    print(f"Data saved to {file_path}")

def data_collection():
    print("fetching translation data")
    train_data = fetch_translation_data(num_samples=10000)
    val_data = fetch_translation_data(num_samples=2000)

    print("saving training and validation data")
    save_data_to_json(train_data,"data/train_data.json")
    save_data_to_json(val_data,"data/val_data.json")

    print("data collection complete")


