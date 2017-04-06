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

DEFAULT_DATA="./multi_classes_image_caption.txt"

def generate_train_test_data():
	input_file= open(DEFAULT_DATA)
	test_file=codecs.open('./pascal_train_dataset.txt','w',encoding='utf-8')
	first_part=codecs.open('./pascal_test_first.txt','w',encoding='utf-8')
	second_part=codecs.open('./pascal_test_second.txt','w',encoding='utf-8')

	line_count=0
	for line in input_file:
		if line!='\n' and line_count==0 or line_count==1:
			#test_data=item[item.find('	')+1:len(item)-1]
			test_file.write(line.decode('utf-8'))
			line_count+=1
			continue
			#test_file.write('\n')
		if line!='\n' and line_count==2:
			#first_data=item[item.find('	')+1:len(item)-1]
			first_part.write(line.decode('utf-8'))
			line_count+=1
			continue
			#first_part.write('\n')
		if line!='\n' and line_count==3:
			#second_data=item[item.find('	')+1:len(item)-1]
			second_part.write(line.decode('utf-8'))
			line_count+=1
			continue
			#second_part.write('\n')
		if not line.strip():
			line_count=0
			continue

###############################################################################################################################################
# main function
if __name__ == '__main__' :
	generate_train_test_data()