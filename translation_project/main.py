import argparse
import os
from src.data_collector import data_collection
from src.data_loader import get_dataset
from train import train_model
from finetune import fine_tune_model
import subprocess

def run_data_pipeline():
    print("\n Starting Data Collection and preprocessing")
    train_data,val_data = get_dataset()

def run_training_pipeline():
    print("Starting Model Training")
    train_model()
    print("Model training complete")

def run_finetuning_pipeline():
    print("Starting fine tuning")
    fine_tune_model()
    print("\n Fine Tuning Complete \n")

def run_deployement_pipeline():
    print("\n Starting model deployement")
    subprocess.run(["python","api.py"])

def run_streamlit_ui():
    print("\n Starting Streamlit UI")
    subprocess.run(["streamlit","run","app.py"])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Pipeline Automation for Translation Model")
    parser.add_argument("--run_all",action="store_true",help="Run all steps in the sequence")
    parser.add_argument("--data",action="store_true",help="Run data Pipeline")
    parser.add_argument("--train",action="store_true",help="Run model training")
    parser.add_argument("--finetune",action="store_true",help="Fine-tune existing model")
    parser.add_argument("--deploy",action="store_true",help="Deploy the model")
    parser.add_argument("--ui",action="store_true", help="Run the Streamlit UI")

    args = parser.parse_args()

    if args.run_all:
        run_data_pipeline()
        run_training_pipeline()
        run_finetuning_pipeline()
        run_deployement_pipeline()
        run_streamlit_ui()
    elif args.data:
        run_data_pipeline()
    elif args.train:
        run_training_pipeline()
    elif args.finetune:
        run_finetuning_pipeline()
    elif args.deploy:
        run_deployement_pipeline()
    elif args.ui:
        run_streamlit_ui()
    else:
        print("No steps specified. Please choose one or more steps using the flags --data, --train, --fintune, --deploy, --ui.")