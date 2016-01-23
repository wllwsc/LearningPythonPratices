# -*- coding: utf8 -*-
import re
import urllib2
import time
import json

def main():
	url = "http://www.gzqcjj.com/bidfile/session.js"
	url1 = "http://jj.gzqcjj.com/carbid/getcurrenttimelong?flag=long&isjsonp=T"
	resp = urllib2.urlopen(url)
	html = resp.read()

	#s = re.search('<h1\s+?id="mainTitle".+(?P<jjdate>\d\d月\d\d日)', html)

	#d = eval(html)
	#print time.ctime(float(d['time']))
	#print time.ctime(float(d['time'])/1000)
	#print time.time()
	print html



if __name__ == "__main__":
	main()



