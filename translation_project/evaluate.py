import sacrebleu
from src.data_loader import get_dataset
from src.model import TranslationModel

_,val_dataset = get_dataset()
model = TranslationModel()

references = val_dataset["target_text"]
hypotheses = [model.translate(text) for text in val_dataset["input_text"]]

bleu = sacrebleu.corpus_bleu(hypotheses,[references])
print(f"BLEU score: {bleu.score}")



