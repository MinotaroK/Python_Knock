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
    if line.count("====") > 0:
        print u"レベル：3" + u"\tセクション:" + line.replace("=", "")
    elif line.count("===") > 0:
        print u"レベル：2" + u"\tセクション:" + line.replace("=", "")
    elif line.count("==") > 0:
        print u"レベル：1" + u"\tセクション:" + line.replace("=", "")
#   m = re.compile('==')
#  s = m.findall(line)
#    print s
    #for n in s:
     #   print n