def play_56():
	s=input('Enter string :')
	ss=input('Enter char :')
	s1=list(s)
	for i in range(len(s1)):
		if s1[i]==ss:
			return i+1
	return -1
play_56()
