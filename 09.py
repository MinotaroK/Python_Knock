import random
import re

def randomly(text):
	text_list = re.split("", text)
	changed = ""
	for i in text_list:
		n = n + 1
		if len(text_list[n]) >= 5
			text_list[n] = random.shuffle(text_list[n])
		changed += text_list[n]
	return changed

text = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

print randomly(text)