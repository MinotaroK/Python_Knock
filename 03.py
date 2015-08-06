import re

text = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
text_list = re.split(", | ", text)

for index,value in enumerate(text_list):
	print len(value)