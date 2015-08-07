import re

text = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
text_list = re.split(", | ", text)
#text = text.replace(".", "")
#text_list = text.split(" ")
text_index = {}

for i, text_list in enumerate(text_list):
	n = i + 1
	if n in [1, 5, 6, 7, 8, 9, 15, 16, 19]:
		text_index[text_list[:1]] = n
	else:
		text_index[text_list[:2]] = n


print(text_index)

#for index,value in enumerate(text_list):
#	print index+1,value[0:1]