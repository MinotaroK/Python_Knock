import re

text = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
text_list = text.replace(".", "")
text_list = re.split(", | ", text)
#text = text.replace(".", "")
#text = text.split(", | ")

for index,value in enumerate(text_list):
	print len(value)