
import os
import sys
import math
import random
import urllib

def load_data(agent_list,ck):
	index = random.randint(0,len(agent_list))
	cookie = {}
	if ck != 'n' or ck != 'N':
		data = {'Cookie':ck,'User-Agent':agent_list[index]}
	data = urllib.urlencode(data)
	return data

def load_post_data(agent_list,ck,param):
	index = random.randint(0,len(agent_list))
	cookie = {}
	if ck != 'n' or ck != 'N':
		data = dict({'Cookie':ck,'User-Agent':agent_list[index]} , **param)
	data = urllib.urlencode(data)
	return data
