# -*- coding: utf-8 -*-
'''
	get user-agent from agent.txt
	for anti anti-spider and bypas  waf 
	youcan also add  your agent in it

'''
import os
import sys

def load_agent():
	agent_list = []
	with open('agent.txt','r') as f:
		content = f.readlines()
		for i in range(0,len(content)):
			agent_list.append(content[i].strip('\n'))
	#print payload_list
	return agent_list