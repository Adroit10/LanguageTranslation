from transformers import MarianMTModel,MarianTokenizer
import torch

class TranslationModel:
    def __init__(self,model_path="./models/fine_tuned_translation_model_v2"):
        # loads tokenizer and model
        self.tokenizer = MarianTokenizer.from_pretrained(model_path)
        self.model = MarianMTModel.from_pretrained(model_path)

    def translate(self, text):
        inputs = self.tokenizer(text,return_tensors="pt",padding=True,truncation=True)
        with torch.no_grad():
            translated_ids = self.model.generate(**inputs)
        return self.tokenizer.decode(translated_ids[0],skip_special_tokens=True)
    
