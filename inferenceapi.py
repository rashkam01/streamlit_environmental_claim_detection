# import requests

# API_URL = "https://api-inference.huggingface.co/models/whispAI/ClaimBuster-DeBERTaV2"
# headers = {"Authorization": f"Bearer {API_TOKEN}"}

# def query(payload):
# 	response = requests.post(API_URL, headers=headers, json=payload)
# 	return response.json()
	
# output = query({
# 	"inputs": "I like you. I love you",
# })



# Construction 1
#from spacy.tokenizer import Tokenizer
#from spacy.lang.en import English

#from spacy.pipeline import Sentencizer

# nlp = English()
# sbd = nlp.create_pipe('sentencizer')
# nlp.add_pipe(sbd)

# text="Please read the analysis. (You'll be amazed.)"
# doc = nlp(text)

# sents_list = []
# for sent in doc.sents:
#    print(sent)
#    #sents_list.append(sent.text)

#print(sents_list)


#from __future__ import unicode_literals, print_function
# from spacy.lang.en import English # updated

# raw_text = 'Hello, world. Here are two sentences.'
# nlp = English()
# nlp.add_pipe(nlp.create_pipe('sentencizer')) # updated
# doc = nlp(raw_text)
# sentences = [sent.string.strip() for sent in doc.sents]

import spacy
nlp = spacy.load('en_core_web_sm')

text = 'My first birthday was great. My 2. was even better.'
for i in nlp(text).sents:
    print(i)


# text = 'My first birthday was great. My 2. was even better.'
# sentences = [i for i in nlp(text).sents]
