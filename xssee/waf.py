# -*- coding: utf-8 -*-

import urllib
import urllib2
import requests
import os
import sys

def waf_detect(target,ck,flag):
	waf_detect_payload = ['search=<script>alert(1)</script>','file=../../../etc/passwd','id=1']