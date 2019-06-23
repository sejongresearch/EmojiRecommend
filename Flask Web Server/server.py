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

app = Flask(__name__)

#################################################################################
# load classes
classes = ['__label__1', '__label__2', '__label__3', '__label__4', '__label__5']

# load words
words=[]
file=open('words.txt','r')
while (1):
    line=file.readline()
    try:escape=line.index('\n')
    except:escape=len(line)
    if line:
        words.append(line[0:escape])
    else:
        break
file.close()

# stem function
stemmer = LancasterStemmer()

# translate
def ko_en_translater(text):
    #! pip install googletrans
    
    translator = Translator()
    result = translator.translate(text, src="ko", dest="en").text
    
    return result

# input sentence
def classify(sentence, show_details=False):
    sentence = ko_en_translater(sentence)
    results = think(sentence, show_details)

    results = [[i,r] for i,r in enumerate(results)]# if r>ERROR_THRESHOLD ] 
    results.sort(key=lambda x: x[1], reverse=True) 
    return_results =[[classes[r[0]],r[1]] for r in results]
    print ("%s \n classification: %s" % (sentence, return_results))
    return return_results

# sigmoid function
def sigmoid(x):
    output = 1/(1+np.exp(-x))
    return output

# sigmoid 함수의 기울기
def sigmoid_output_to_derivative(output):
    return output*(1-output)

# 문장 토큰화 및 stem화
def clean_up_sentence(sentence):
    # tokenize화
    sentence_words = nltk.word_tokenize(sentence)
    # 단어 stem화
    sentence_words = [stemmer.stem(word.lower()) for word in sentence_words]
    return sentence_words

# bow값 반환: 문장에 해당 단어가 있으면 1 반환, 아니면 0 반환
def bow(sentence, words, show_details=False):
    # clean_up_sentence()를 사용하여 문장 토큰화 및 stem화
    sentence_words = clean_up_sentence(sentence)
    # bow 제작
    bag = [0]*len(words)  
    for s in sentence_words:
        for i,w in enumerate(words):
            if w == s: 
                bag[i] = 1
                if show_details:
                    print ("found in bag: %s" % w)

    return(np.array(bag))


def think(sentence, show_details=False):
    x = bow(sentence.lower(), words, show_details)
    if show_details:
        print ("sentence:", sentence, "\n bow:", x)
    # layer0: 입력값들은 words
    l0 = x
    # layer1: layer0과 synapse0 행렬곱
    l1 = sigmoid(np.dot(l0, synapse_0))
    # layer2: layer1과 synapse1 행렬곱 이후 리턴
    l2 = sigmoid(np.dot(l1, synapse_1))
    return l2


ERROR_THRESHOLD = 0.2
synapse_file = './model/synapses.json' 

with open(synapse_file, 'r') as data_file:
	synapse = json.load(data_file)
	synapse_0 = np.asarray(synapse['synapse0'])
	synapse_1 = np.asarray(synapse['synapse1'])
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
	result = dict(classify(result))
	return render_template('index.html', result=result)

if __name__ == '__main__':
	app.run(debug=True)