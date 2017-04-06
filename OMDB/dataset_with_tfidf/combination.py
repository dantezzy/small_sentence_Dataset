#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-12-13 12:02:33
# @Author  : Ziyi Zhao
# @Link    : http://example.org
# @Version : 1.0

import os

original = open("./proceed_dataset_OMDB_100_20_original.txt","r")
original_title = open("./proceed_dataset_OMDB_100_20_origianl_title.txt","r")
original_title_tag = open("./proceed_dataset_OMDB_100_20_original_title_tag.txt","r")

proceed_original = open("./original.txt","w")
proceed_original_title = open("./original_title.txt","w")
proceed_original_title_tag = open("./original_title_tag.txt","w")

count=0
input_data=[]
for doc in original:
	for text in doc:
	    temp_str=''
	    for i in xrange(0,len(doc)-1):
	        temp_str+=doc[i]
	        temp_str+=' '
	    if len(doc)-1>0:
	        temp_str+=doc[len(doc)-1]
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
proceed_original = open("./original.txt","w")
for item in input_data:
    proceed_original.write("%s\n" % item)