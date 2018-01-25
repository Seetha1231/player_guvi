def play_27():
	s=input()
	l=list(s)
	res=""
	for i in range(len(l)):
		if ord(l[i]) in range(65,91):
			q=ord(l[i])+32
			res+=chr(q)
		elif ord(l[i]) in range(97,122):
			q=ord(l[i])-32
			res+=chr(q)
		else :
			res+=l[i]
	print(res)
play_27()
