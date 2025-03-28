
from transformers import MarianMTModel,MarianTokenizer,TrainingArguments,Trainer
from src.data_loader import get_dataset

def train_model():
    train_dataset,val_dataset = get_dataset()

    model_name = "Helsinki-NLP/opus-mt-en-es"
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = MarianMTModel.from_pretrained(model_name)


    # training arguments
    training_args = TrainingArguments(
        output_dir="./models/fine_tuned_translation_model_v2",
        evaluation_strategy="epoch",
        save_strategy="epoch",
        per_device_train_batch_size=8,
        per_device_eval_batch_size=8,
        logging_dir="./logs",
        num_train_epochs=3,
        learning_rate=5e-5,
        weight_decay=0.01
    )

    trainer = Trainer(
        model = model,
        args=training_args,
        train_dataset=train_dataset,
        eval_dataset=val_dataset
    )
    trainer.train()

    model.save_pretrained("./models/fine_tuned_translation_model_v2")
    tokenizer.save_pretrained("./models/fine_tuned_translation_model_v2")
    print("model fine tuned and saved")

