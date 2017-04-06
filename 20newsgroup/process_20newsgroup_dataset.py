#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-11-08 16:33:33
# @Author  : Ziyi Zhao


import os
import nose
import numpy
import scipy
import gensim
import logging
import math
import sys 
import string
import pickle
from nltk.corpus import stopwords
# for word tense
from nltk.stem import PorterStemmer, WordNetLemmatizer
# for TF-IDF
import sklearn
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer

from nltk.tokenize import RegexpTokenizer
from gensim import corpora
import numpy
import cPickle as pickle
import regex as re
import random

import tarfile
import codecs

categories = ['alt.atheism', 'comp.graphics', 'comp.os.ms-windows.misc', 'comp.sys.ibm.pc.hardware', 'comp.sys.mac.hardware',
              'comp.windows.x', 'misc.forsale', 'rec.autos', 'rec.motorcycles', 'rec.sport.baseball', 'rec.sport.hockey', 
              'sci.crypt', 'sci.electronics', 'sci.med', 'sci.space', 'soc.religion.christian', 'talk.politics.guns', 
              'talk.politics.mideast', 'talk.politics.misc', 'talk.religion.misc']

def import_raw_data():

	with tarfile.open('./20news-bydate-test.tar.gz', 'r:gz') as tf:
	    # get information (metadata) about all files in the tarball
	    file_infos = [file_info for file_info in tf if file_info.isfile()]
	    
	    # print one of them; for example, the first one
	    message = tf.extractfile(file_infos[0]).read()
	    #print(message)
	    print len(file_infos)

	    count = 0
		#raw texts
	    data = []
	    for element in file_infos:
			message = tf.extractfile(element).read()
			string = process_message(message)
			#print 'Doc:',count
			#print ('\n')
			#print(string)
			data.append(string.lower())
			#print ('\n')
			count+=1

	    return data

def process_message(message):
    """
    Preprocess a single 20newsgroups message, returning the result as
    a unicode string.
    
    """
    message = gensim.utils.to_unicode(message, 'latin1').strip()
    blocks = message.split(u'\n\n')
    # skip email headers (first block) and footer (last block)
    content = u'\n\n'.join(blocks[1:])
    return content

#check if word contains punctuations or digits
def isContainPorD(s):
    return re.search(r'(\d|\p{P})', s)

def process_data(data):
	tokenizer = RegexpTokenizer(r'\w+')
	# preprocessed texts
	texts=[]

	# Create English stop words
	stopset = stopwords.words('english')
	print len(data)

	count = 0
	#loop through document list
	for docu in data:
	    #remove stop words and digits and punctuations
	    removed_tokens = [i for i in tokenizer.tokenize(docu) if i not in stopset and not isContainPorD(i)]
	    #preprocessed texts
	    texts.append(removed_tokens)
	    count +=1

	count=0
	input_data=[]
	for text in texts:
	    temp_str=''
	    for i in xrange(0,len(text)-1):
	        temp_str+=text[i]
	        temp_str+=' '
	    #temp_str+=text[len(text)-1]
	    #print(temp_count)
	    input_data.append(temp_str.encode('ascii', 'ignore'))
	    #print(count)
	    #print ('\n')
	    # print (temp_str)
	    # print ('\n')
	    count+=1

	#save input result
	newOpenFile=open("20newsgroups_test_dataset.txt","w")
	for item in input_data:
	    newOpenFile.write("%s\n" % item)
	print ("finish!")

###############################################################################################################################################
# main function
if __name__ == '__main__' :
	data = import_raw_data()
	process_data(data)
