import os
import urllib
import urllib2
import urlparse
import requests
from payload import load
import webbrowser
import time
from agent import load_agent
import math
from common import load_post_data




def post_detect(target,ck,flag,param,waf):
	payload = load()
	agent = load_agent()

	host = target

	for i in range(0,len(payload)):
		if waf == True:
			time.sleep(0.5)
			try:
				urllib2.urlopen(host)
			except:
				pass
			time.sleep(0.5)
		for j in param.keys():
			if flag in param[j]:
				exp = flag + payload[i]
				param[j] = param[j].replace(flag,exp)
				try:
					post_data = load_post_data(agent,ck,param)

					req = urllib2.Request(target,data = post_data)
					res = urllib2.urlopen(req)
					content_html = res.read()
					if exp in content_html or payload[i] in content_html:
						print '[!]success wtih payload',param[j]
						#post_detect(target,ck,flag,param_dict,True)
						
				except:
					pass
				param[j] = param[j].replace(exp,flag)

