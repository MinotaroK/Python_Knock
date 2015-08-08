def word_ngram(my_sent, n):
	words_bi_list = []
	words = ["<s>"] + my_sent.split()
	words.append("</s>")
	for i in range(len(words) - n + 1):
		words_bi_list.append(words[i:i+n])
	return words_bi_list


def char_ngram(my_sent, n):
    char_bi_list = []
    for i in range(len(my_sent) -n +1):
        if my_sent[i] == " " or my_sent[i+1] == " ": continue
        char_bi_list.append(my_sent[i:i+n])
    return char_bi_list



if __name__ == '__main__':
    my_sent = "paraparaparadise"
    X1 = word_ngram(my_sent, 2)
    X2 = char_ngram(my_sent, 2)



if __name__ == '__main__':
    my_sent = "paragraph"
    Y1 = word_ngram(my_sent, 2)
    Y2 = char_ngram(my_sent, 2)

 