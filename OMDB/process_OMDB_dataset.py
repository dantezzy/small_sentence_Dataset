#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-11-07 14:14:57
# @Author  : Ziyizhao

import os
import csv
import logging
import math
import string
import sys 
import re
import os
import codecs
from pprint import pprint
DEFAULT_DATA="./OMDB_dataset.txt"

def generate_train_test_data():
	input_file= open(DEFAULT_DATA)
	test_file=codecs.open('./OMDB_train_dataset.txt','w',encoding='utf-8')
	first_part=codecs.open('./OMDB_test_dataset.txt','w',encoding='utf-8')

	test_file_tag=codecs.open('./OMDB_train_dataset_tag.txt','w',encoding='utf-8')
	first_part_tag=codecs.open('./OMDB_test_dataset_tag.txt','w',encoding='utf-8')

	test_file_title=codecs.open('./OMDB_train_dataset_title.txt','w',encoding='utf-8')
	first_part_title=codecs.open('./OMDB_test_dataset_title.txt','w',encoding='utf-8')


	title_dict = dict()
	tag_dict = dict()

	title_file=open('./OMDB_title.txt','r')
	title_number = 0
	for title in title_file:
		title_dict.update({title_number:title})
		title_number += 1

	tag_file=open('./OMDB_tag.txt','r')
	tag_number = 0
	for tag in tag_file:
		tag_dict.update({tag_number:tag})
		tag_number += 1

	line_count=0
	for item in input_file:
		if item!='\n' and line_count<7000:
			#test_data=item[item.find('	')+1:len(item)-1]
			test_file.write(item.decode('utf-8'))
			test_file_tag.write(str(tag_dict[line_count]))
			test_file_title.write(str(title_dict[line_count]))
			#test_file.write('\n')
		if item!='\n' and line_count>=7000:
			#first_data=item[item.find('	')+1:len(item)-1]
			first_part.write(item.decode('utf-8'))
			first_part_tag.write(str(tag_dict[line_count]))
			first_part_title.write(str(title_dict[line_count]))
			#first_part.write('\n')
		line_count+=1

def generate_ID():

	test_file_ID=codecs.open('./OMDB_train_dataset_ID.txt','w',encoding='utf-8')
	first_part_ID=codecs.open('./OMDB_test_dataset_ID.txt','w',encoding='utf-8')

	# ID_dict = dict()

	ID_file=open('./OMDB_movieID.txt','r')
	# ID_number = 0
	# for ID in ID_file:
	# 	ID_dict.update({ID_number:ID})
	# 	ID_number += 1

	line_count=1
	for item in ID_file:
		print line_count
		if line_count<=7000:
			test_file_ID.write(item)
		if line_count>7000:
			first_part_ID.write(item)
		line_count+=1

###############################################################################################################################################
# main function
if __name__ == '__main__' :
	generate_train_test_data()
	#generate_ID()