#coding: UTF-8

def engine(x, y, z):
	text = "%s時の%sは%s" % (x, y, z)
	return text

#if __name__ == '__main__':
#	x = 14
#	y = "気温"
#	z = 22.4
print engine(14, "気温", 22.4)