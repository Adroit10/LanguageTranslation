from transformers import MarianMTModel, MarianTokenizer, TrainingArguments, Trainer
from src.data_loader import get_dataset
import os

def fine_tune_model():
    train_dataset,val_dataset = get_dataset()

    model_path = "./models/fine_tuned_translation_model_v2"
    if os.path.exists(model_path):
        tokenizer = MarianTokenizer.from_pretrained(model_path)
        model=MarianMTModel.from_pretrained(model_path)
        print("loaded pre-trained model for fine tuning")

    else:
        print("No fine-tuned model found! Training from scratch instead")
        model_name = "Helsinki-NLP/opus-mt-en-es"
        tokenizer = MarianTokenizer.from_pretrained(model_name)
        model = MarianMTModel.from_pretrained(model_name)
        training_args = TrainingArguments(
            output_dir=model_path,
            evaluation_strategy="epoch",
            save_strategy="epoch",
            per_device_train_batch_size=8,
            per_device_eval_batch_size=8,
            logging_dir="./logs",
            num_train_epochs=2,
            warmup_steps=2e-5,
            weight_decay=0.01,
        )
        trainer = Trainer(
            model=model,
            args=training_args,
            train_dataset=train_dataset,
            eval_dataset=val_dataset)
        trainer.train()
        model.save_pretrained(model_path)
        tokenizer.save_pretrained(model_path)