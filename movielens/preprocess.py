from __future__ import print_function
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from nltk.stem.porter import PorterStemmer
from gensim import corpora
import csv
import numpy
import cPickle as pickle
import regex as re
import random

#raw texts
data=[]
title=[]
tag=[]

# read CSV file
data_file_name = "moviesDetail.csv"
with open(data_file_name, "rb") as csvfile:
    reader = csv.reader(csvfile)
    for index, row in enumerate(reader):
        if len (row) > 3:
            space_count=row[3].count(' ')
            if space_count > 5:
                title.append(unicode(row[1], errors='ignore').lower())
                tag.append(unicode(row[2], errors='ignore').lower())
                temp_str = ''
                temp_str += unicode(row[1], errors='ignore').lower()
                temp_str += ' '
                temp_str += unicode(row[2], errors='ignore').lower()
                temp_str += ' '
                temp_str += unicode(row[3], errors='ignore').lower()
                #data.append(unicode(row[2], errors='ignore').lower())
                #data.append(unicode(row[3], errors='ignore').lower())
                data.append(temp_str)

#number of documents
num_of_doc=len(data)
print (num_of_doc)

tokenizer = RegexpTokenizer(r'\w+')
# preprocessed texts
texts=[]

# Create English stop words
stopset = stopwords.words('english')

#check if word contains punctuations or digits
def isContainPorD(s):
    return re.search(r'(\d|\p{P})', s)

#loop through document list
for doc in data[0:]:
    #remove stop words and digits and punctuations
    removed_tokens = [i for i in tokenizer.tokenize(doc) if i not in stopset and not isContainPorD(i)]
    #preprocessed texts
    texts.append(removed_tokens)

count=0
input_data=[]
for text in texts:
    temp_str=''
    for i in xrange(0,len(text)-2):
        temp_str+=text[i]
        temp_str+=' '
    if len(text)-1>0:
        temp_str+=text[len(text)-1]
    #print(temp_count)
    input_data.append(temp_str)
    print(count)
    print ('\n')
    print (temp_str)
    print ('\n')
    count+=1

input_title=[]
for title in title[0:]:
    input_title.append(title)

input_tag=[]
for tag in tag[0:]:
    input_tag.append(tag)

#save input result
newOpenFile=open("movielens_dataset.txt","w")
for item in input_data:
    newOpenFile.write("%s\n" % item)

newOpenFile_title=open("movielens_title.txt","w")
for title in input_title:
    newOpenFile_title.write("%s\n" % title)

newOpenFile_tag=open("movielens_tag.txt","w")
for tag in input_tag:
    newOpenFile_tag.write("%s\n" % tag)

print ("finish!")