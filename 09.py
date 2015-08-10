import random
import re

def randomly(text):
	text_list = re.split("", text)
	changed = ""
	for i in text_list:
		if len(text_list) >= 5
			text_list = random.shuffle(text_list)
		changed += text_list
	return changed

text = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

print randomly(text)