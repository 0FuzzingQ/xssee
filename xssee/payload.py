# -*- coding: utf-8 -*-
'''
	get xss payload from payload.txt
	youcan also add  your payload in it

'''
import os
import sys

def load():
	payload_list = []
	with open('payload.txt','r') as f:
		content = f.readlines()
		for i in range(0,len(content)):
			payload_list.append(content[i].strip('\n'))
	#print payload_list
	return payload_list

