
import sys
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
from common import load_data




def get_detect(target,ck,flag,waf):
	payload = load()
	agent = load_agent()

	host = target.split('?')[0]

	for i in range(0,len(payload)):
		if waf == True:
			time.sleep(0.5)
			try:
				urllib2.urlopen(host)
			except:
				pass
			time.sleep(0.5)

		exp = flag + str(payload[i])
		now_target = target.replace(flag,exp)
		#print now_target
		try:
			data = load_data(agent,ck)
			req = urllib2.Request(now_target,data = data)
			res = urllib2.urlopen(req)
			content_html = res.read()
			if waf == True:
				time.sleep(0.5)
				try:
					urllib2.urlopen(host)
				except:
					pass
				time.sleep(0.5)
			#print content_html
			if exp in content_html or str(payload[i]) in content_html:
				#print 'aaa'
				#webbrowser.open(now_target)
				print '[*]find payload success!',now_target
				#exit()
			else:
				pass
				#print '[*]find payload failed!',now_target
		except:
			pass



	

