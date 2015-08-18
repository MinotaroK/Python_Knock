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
	if line.find('Category') >= 0:
		print re.split(":", line)
