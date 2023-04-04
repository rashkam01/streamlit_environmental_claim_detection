import streamlit as st
from transformers import pipeline
#from PIL import Image
import spacy

nlp = spacy.load('en_core_web_sm')

pipeline = pipeline(task="text-classification", model="rashmikamath01/distillbert-fine-tuned-claimbuster3C")

st.title(" Are there any check worthy claims within your text ? ")
claim_input = st.text_input(label='Type your claim here: ')


st.header("Check worthy Claims are the following: ")
for i in nlp(claim_input).sents:
    #st.header(i)
    sent = str(i)
    predictions = pipeline(sent)
    for p in predictions:    
        #st.subheader(f"{ p['label'] }: { round(p['score'] * 100, 1)}%")
        #st.subheader(sent)
        if p['label'] == 'Claim':
            st.subheader(sent)
            st.subheader(f"{ p['label'] }: { round(p['score'] * 100, 1)}%")
