#coding: UTF-8

def cipher(word):
	changed = ""
	for char in word:
		if char.islower():
			char = chr(219 - ord(char))
		changed += char
	return changed

word = "I want to eat some Vegetables"
print cipher(word)