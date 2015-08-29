#coding: utf-8

import gzip
import json
import re

f = gzip.open('./jawiki-country.json.gz', 'rb')
file_gz = f.read()
f.close()

article = {}

for line in file_gz.splitlines():
    at_line = json.loads(line)
    article[at_line['title']] = at_line

england = article[u'イギリス']['text']

for line in england.splitlines():
	#pattern = re.compile(r'^[0-9A-Za-z]+$')
	#result = pattern.findall(line)
	#if result:
	#	print result
	
	if line.find(u"ファイル") > 0:
		str1 =  line.split("|")[0].replace("]", "").replace("[", "").replace(u"ファイル:", "")
		str2 =  line.split("|")[1].replace("]", "").replace("[", "").replace("thumb", "").replace(u"国章画像 = ", "").replace(u"ファイル:", "")
		str3 =  line.split("|")[3].replace("]", "").replace("[", "")
		str4 =  str1 + "\t" + str2 + "\t" + str3
		print str4.strip()
