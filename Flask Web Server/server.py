# -*- coding: utf-8 -*-

from flask import Flask, render_template, request
import nltk
from nltk.stem.lancaster import LancasterStemmer
import os
import json
import datetime
import pandas as pd
from soynlp.normalizer import *
import numpy as np
import time
import re
from googletrans import Translator
import json
import re, sys, os, csv, keras, pickle
from keras import regularizers, initializers, optimizers, callbacks
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.utils.np_utils import to_categorical
from keras.layers import Embedding
from keras.layers import Dense, Input, Flatten, Concatenate
from keras.layers import Conv1D, MaxPooling1D, Embedding, Add, Dropout, LSTM, GRU, Bidirectional
from keras.models import Model
from keras import backend as K
from keras.engine.topology import Layer, InputSpec
from keras.models import load_model
from sklearn.metrics import classification_report, confusion_matrix
import numpy as np
import itertools, pickle
from keras.models import model_from_json 
from flask_phantom_emoji import PhantomEmoji

app = Flask(__name__)
PhantomEmoji(app)

#################################################################################
# load classes
classes = [" 😍, 😘, 😙", "😤, 😡, 😠", "😥, 😢, 😭", "😔, 😑, 😐", "😨, 😰, 😱"]
# translate
def ko_en_translater(text):
    #! pip install googletrans
    translator = Translator()
    result = translator.translate(text, src="ko", dest="en").text
    
    return result
    
def word_emoticon(text):
    emoticon = {'flower':'🌸', 'soccer':'⚽', 'movie':'🎬', 'money':'💵', 'grape':'🍇', 'makeup':'💄', 'orange':'🍊', 'baby':'👶', 'chicken':'🐔', 'recycle':'♻', 'perfect':'💯', 'sun':'🌞', 'flight':'✈', 'music':'🎵', 'star':'⭐', 'pizza':'🍕', 'christmas':'🎄', 'moon':'🌙', 'earth':'🌏', 'cake':'🍰', 'photo':'📷', 'clap':'👏', 'hi':'✋', 'muah':'💋', 'melong': '👅', 'present': '🎁'}
    keys = ['flower', 'soccer', 'movie', 'money', 'grape', 'makeup', 'orange', 'baby', 'chicken', 'recycle', 'perfect', 'sun', 'flight', 'music', 'star', 'pizza', 'christmas', 'moon', 'earth', 'cake', 'photo', 'clap', 'hi', 'muah', 'melong', 'present']
    result = []
    for key in keys:
        if key in text:
            result.append(emoticon[key])
    
    return result


def classify(text):
    emoji = word_emoticon(text)
    text = ko_en_translater(text)
    tokenizer = Tokenizer(num_words=40000)
    sequences_test = tokenizer.texts_to_sequences(text)
    data_int_t = pad_sequences(sequences_test, padding='pre', maxlen=(MAX_SEQUENCE_LENGTH-5))
    data_test = pad_sequences(data_int_t, padding='post', maxlen=(MAX_SEQUENCE_LENGTH))
    json_file = open("./model/model.json", "r") 
    loaded_model_json = json_file.read() 
    json_file.close() 
    loaded_model = model_from_json(loaded_model_json)
    loaded_model.load_weights("./model/model.h5") 
    y_prob = loaded_model.predict(data_test)
    for n, prediction in enumerate(y_prob):
        pred = y_prob.argmax(axis=-1)[n]
        print(text[n],"\nPrediction:",classes[pred],"\n")
    
    result = classes[pred]
    
    for i in range(len(emoji)):
        result = result + "," + emoji[i] + " "
        
    return result


MAX_NB_WORDS = 40000 # max no. of words for tokenizer
MAX_SEQUENCE_LENGTH = 30 # max length of text (words) including padding
VALIDATION_SPLIT = 0.2
EMBEDDING_DIM = 200 # embedding dimensions for word vectors (word2vec/GloVe)
###############################################################################
@app.route("/", methods=['GET', 'POST'])
def index():
    # 일반적으로 접속 
    if request.method == 'GET':
        return render_template('index.html')

    # 데이터 입력
    if request.method == 'POST':
        result = request.form['result']


    sentence = "__label__1"
    result = classify(result)
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
