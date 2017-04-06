#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-09-14 23:40:35
# @Author  : Ziyi Zhao (zzhao37@syr.edu)
# @Version : 1.0

import os
import logging
import math
import string
import json
import sys 
import re
import os
import codecs
from pprint import pprint

DEFAULT_PATH="./flicker/results_20130124.token"
DEFAULT_DATA="./flicker/flicker_dataset.txt"

def readrawdata():
# get file name segment
	segment=DEFAULT_PATH.split('/')
	name_with_dot=segment[len(segment)-1]
	print("\nProcessing "+name_with_dot+" dataset")

# delete .
	purefilename=name_with_dot.split('.')
	filename=purefilename[0]
	dataset_file=codecs.open('./flicker/flicker_dataset.txt','w',encoding='utf-8')


# open original file
	with open(DEFAULT_PATH) as data_file:
		for item in data_file:
			if item != 0:
				#print(item)
				#print('\n')
				seg=item.split('#')
				real_data=seg[len(seg)-1]
				dataset_file.write(real_data.decode('utf-8'))
				dataset_file.write('\n')

def generate_train_test_data():
	input_file= open(DEFAULT_DATA)
	test_file=codecs.open('./flicker/flicker_train_dataset.txt','w',encoding='utf-8')
	first_part=codecs.open('./flicker/flicker_test_first.txt','w',encoding='utf-8')
	second_part=codecs.open('./flicker/flicker_test_second.txt','w',encoding='utf-8')

	line_count=0
	for item in input_file:
		if item!='\n' and item[0]=='0' or item[0]=='1':
			test_data=item[item.find('	')+1:len(item)-1]
			test_file.write(test_data.decode('utf-8'))
			test_file.write('\n')
		if item!='\n' and item[0]=='2' and line_count<10000:
			first_data=item[item.find('	')+1:len(item)-1]
			first_part.write(first_data.decode('utf-8'))
			first_part.write('\n')
		if item!='\n' and item[0]=='3' and line_count<10000:
			second_data=item[item.find('	')+1:len(item)-1]
			second_part.write(second_data.decode('utf-8'))
			#.encode('utf-8')
			second_part.write('\n')
		line_count+=1

###############################################################################################################################################
# main function
if __name__ == '__main__' :
	readrawdata()
	generate_train_test_data()