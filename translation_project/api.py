from fastapi import FastAPI
from pydantic import BaseModel
from src.model import TranslationModel

app = FastAPI()
translator = TranslationModel()

class TranslationRequest(BaseModel):
    text:str

@app.post("/translate")
def translate_text(request:TranslationRequest):
    translated_text = translator.translate(request.text)
    return {"source text": request.text, "translated text": translated_text}


