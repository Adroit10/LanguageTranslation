
import streamlit as st
from src.model import TranslationModel

translator = TranslationModel()

st.title("Language translator")
st.write("Translate English language to Spanish using a fine_tuned model")

input_text = st.text_area("Enter Text to translate")

if st.button("Translate"):
    if input_text.strip():
        translated_text= translator.translate(input_text)
        st.subheader("Translated Text")
        st.write(translated_text)
    else:
        st.warning("Please enter text to translate")
        

