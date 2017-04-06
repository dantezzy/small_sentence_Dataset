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
real_doc_ID=[]

# read CSV file
data_file_name = "raw-data.csv"
with open(data_file_name, "rb") as csvfile:
    reader = csv.reader(csvfile)
    for index, row in enumerate(reader):
        if len (row) > 4:
            space_count=row[4].count(' ')
            if space_count > 20:
            	real_doc_ID.append(unicode(row[0], errors='ignore').lower())
                data.append(unicode(row[4], errors='ignore').lower())
                title.append(unicode(row[3], errors='ignore'))

#number of documents
num_of_doc=len(data)
print (num_of_doc)

tokenizer = RegexpTokenizer(r'\w+')
# preprocessed texts
texts=[]

# Create English stop words
stopset = []

#check if word contains punctuations or digits
def isContainPorD(s):
    return re.search(r'(\d|\p{P})', s)

#loop through document list
for docu in data[0:]:
    #remove stop words and digits and punctuations
    removed_tokens = [i for i in tokenizer.tokenize(docu) if i not in stopset and not isContainPorD(i)]
    #preprocessed texts
    texts.append(removed_tokens)

count=0
input_data=[]
for text in texts:
    temp_str=''
    for i in xrange(0,len(text)-1):
        temp_str+=text[i]
        temp_str+=' '
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

input_docID=[]
for doc_ID in real_doc_ID[0:]:
    input_docID.append(doc_ID)

#save input result
newOpenFile=open("citeUlike_dataset.txt","w")
for item in input_data:
    newOpenFile.write("%s\n" % item)

newOpenFile_title=open("citeUlike_title.txt","w")
for title in input_title:
    newOpenFile_title.write("%s\n" % title)

newOpenFile_doc_ID=open("citeUlike_docID.txt","w")
for doc_ID in input_docID:
    newOpenFile_doc_ID.write("%s\n" % doc_ID)

print ("finish!")