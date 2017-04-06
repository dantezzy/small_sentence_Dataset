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
DEFAULT_DATA="./citeUlike_dataset.txt"

def generate_train_test_data():
	input_file= open(DEFAULT_DATA)

	test_file=codecs.open('./citeUlike_train_dataset.txt','w',encoding='utf-8')
	first_part=codecs.open('./citeUlike_test_dataset.txt','w',encoding='utf-8')

	test_file_title=codecs.open('./citeUlike_train_dataset_title.txt','w',encoding='utf-8')
	first_part_title=codecs.open('./citeUlike_test_dataset_title.txt','w',encoding='utf-8')

	test_file_ID=codecs.open('./citeUlike_train_dataset_ID.txt','w',encoding='utf-8')
	first_part_ID=codecs.open('./citeUlike_test_dataset_ID.txt','w',encoding='utf-8')

	title_dict = dict()

	title_file=open('./citeUlike_title.txt','r')
	title_number = 0
	for title in title_file:
		title_dict.update({title_number:title})
		title_number += 1

	id_dict = dict()

	id_file=open('./citeUlike_docID.txt','r')
	id_number = 0
	for _id in id_file:
		id_dict.update({id_number:_id})
		id_number += 1

	line_count=0
	for item in input_file:
		if item!='\n' and line_count<14000:
			#test_data=item[item.find('	')+1:len(item)-1]
			test_file.write(item.decode('utf-8'))
			test_file_title.write(str(title_dict[line_count]))
			test_file_ID.write(str(id_dict[line_count]))
			#test_file.write('\n')
		if item!='\n' and line_count>=14000:
			#first_data=item[item.find('	')+1:len(item)-1]
			first_part.write(item.decode('utf-8'))
			first_part_title.write(str(title_dict[line_count]))
			first_part_ID.write(str(id_dict[line_count]))
			#first_part.write('\n')
		line_count+=1

###############################################################################################################################################
# main function
if __name__ == '__main__' :
	generate_train_test_data()