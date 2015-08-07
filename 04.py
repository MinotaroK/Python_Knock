import re

text = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
text_list = re.split(", | ", text)

for index,value in enumerate(text_list):
	print index+1,value[0:1]