from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer
from pprint import pprint
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import wordpunct_tokenize as wordpunct_tokenize
import re
import string
import time
import math

import os
import nose
import numpy
import scipy
import gensim
import logging
import math
import sys 
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

if __name__ == '__main__':
    newsgroups_train = fetch_20newsgroups(subset='train')
    newsgroups_test = fetch_20newsgroups(subset='test')
    pprint(newsgroups_test.filenames.shape)

    stemmer = PorterStemmer()

    def get_stopwords():
        return [u'i', u'me', u'my', u'myself', u'we', u'our', u'ours', u'ourselves', u'you', u'your', u'yours',
                u'yourself',
                u'yourselves', u'he', u'him', u'his', u'himself', u'she', u'her', u'hers', u'herself', u'it', u'its',
                u'itself',
                u'they', u'them', u'their', u'theirs', u'themselves', u'what', u'which', u'who', u'whom', u'this',
                u'that',
                u'these',
                u'those', u'am', u'is', u'are', u'was', u'were', u'be', u'been', u'being', u'have', u'has', u'had',
                u'having', u'do',
                u'does', u'did', u'doing', u'a', u'an', u'the', u'and', u'but', u'if', u'or', u'because', u'as',
                u'until',
                u'while',
                u'of', u'at', u'by', u'for', u'with', u'about', u'against', u'between', u'into', u'through', u'during',
                u'before',
                u'after', u'above', u'below', u'to', u'from', u'up', u'down', u'in', u'out', u'on', u'off', u'over',
                u'under',
                u'again', u'further', u'then', u'once', u'here', u'there', u'when', u'where', u'why', u'how', u'all',
                u'any', u'both',
                u'each', u'few', u'more', u'most', u'other', u'some', u'such', u'no', u'nor', u'not', u'only', u'own',
                u'same', u'so',
                u'than', u'too', u'very', u's', u't', u'can', u'will', u'just', u'don', u'should', u'now']
    #tokenizer for removing stopwords and stemming
    def stemmed_words(d):
        attribute_names = [stemmer.stem(token.lower()) for token in wordpunct_tokenize(
            re.sub('[%s]' % re.escape(string.punctuation), '', d)) if
                        token.lower() not in get_stopwords()]
        return attribute_names


    texts = []#words after preprocessed for each doc
    document = []
    input_data=[]
    count = 0
    for d in newsgroups_test.data:
    	temp = stemmed_words(d)
        texts.append(temp)

    for text in texts:
        if len(text)!=0:
            temp_str = ''
            for i in xrange(0,len(text)-2):
                temp_str += text[i]
                temp_str += ' '
            temp_str += text[len(text)-1]
            document.append(temp_str)

    for doc in document:
        message = gensim.utils.to_unicode(doc, 'latin1').strip()
        print "Doc:",count
        print message
        input_data.append(message.encode('ascii', 'ignore'))
        print "\n"
        count += 1

    newOpenFile=open("20newsgroups_test_dataset.txt","w")
    for item in input_data:
        newOpenFile.write("%s\n" % item)
    print ("finish!")









