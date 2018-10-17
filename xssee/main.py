
import sys
import os
import urllib
import urllib2
import urlparse
import requests
from get import get_detect
from post import post_detect
from  common import load_data,load_post_data
from agent import load_agent
import re
from bs4 import BeautifulSoup

method = ''
flag = 'q0w1e2'

agent_list = load_agent()


def get_fuzzing(target,ck,data):
	print '[*]now demo test get xss......'
	parsed_tuple = urlparse.urlparse(urllib.unquote(target))
	url_query = urlparse.parse_qs(parsed_tuple.query,True)
	print url_query
	for i in url_query.keys():
		query = str(i) + '=' + str(url_query[i][0])
		tmp = query + flag
		location = str(url_query[i][0]) + flag
		
		now_target = target.replace(query,tmp)
		#data = load_data(agent_list,ck)
		try:
			#print 1
			data = load_data(agent_list,ck)
			#print data
			req = urllib2.Request(now_target,data = data)
			#print 3
			res = urllib2.urlopen(req)
			#print 4
			content_html = res.read()
			#print 5
			if flag in content_html or location in content_html:
				#print 6
				get_detect(now_target,ck,flag,True)
			else:
				return False
		except:
			pass
def post_fuzzing(target,ck,data):
	print '[*]now demo test post xss......'
	try:
		data = load_data(agent_list,ck)
		req = urllib2.Request(target,data=data)
		res = urllib2.urlopen(req)
		content = res.read()
		if res.code == 301 or res.code == 302:
			print '[*]we get a 301/302 when connect to the target,please recheck it'
			exit()
		elif res.code == 200:
			param_method = raw_input('[*]you can provide params for accuracy or auto find by xssee: [0]provide [1]auto')
			if param_method == '1':
				print 'now detect params......'
				content = BeautifulSoup(content,'html.parser')
				#print '111'
				input_list = content.select('input')
				for i in range(0,len(input_list)):
					name = input_list[i]['name']
					in_type = input_list[i]['type']
					print name,in_type
			elif param_method == '0':
				print '[*]post data like: id=1&name=2 etc'
				post_str = raw_input('[*]please input post data:')
				param_list = post_str.strip().split('&')
				param_dict = {}
				
				for i in range(0,len(param_list)):
					param_dict[param_list[i].strip().split('=')[0]] = param_list[i].strip().split('=')[1]
				for i in param_dict.keys():
					param_dict[i] = param_dict[i] + flag
					#post_data = urllib.urlencode(param_dict)
					try:
						post_data = load_post_data(agent_list,ck,param_dict)

						req = urllib2.Request(target,data = post_data)
						res = urllib2.urlopen(req)
						content_html = res.read()
						if flag in content_html or param_list[i] in content_html:
							print 'ok!'
							post_detect(target,ck,flag,param_dict,True)
						param_dict[i] = param_dict[i].replace(flag,'')
						
					except:
						pass
						#print '[*]fuzz post test lose connect'

	except:
		print '[*]connect failed to target'
		exit()
			


target = raw_input('[*]please enter the url ou want to test:')
ck = raw_input('[*]please enter the cookie ; if exists , enter n/N:')
data = load_data(agent_list,ck)
try:
	data = load_data(agent_list,ck)
	req = urllib2.Request(target,data = data)

	res = urllib2.urlopen(req)
except:
	pass
	#print '[*]can not connect to target , please check'

if '=' in target:
	method = 'GET'
else:
	method = 'POST'

if method == 'GET':
	get_fuzzing(target,ck,data)

elif method == 'POST':
	post_fuzzing(target,ck,data)