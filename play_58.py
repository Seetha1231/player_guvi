 def play_58():
	s=input('Enter word :')
	ss=input('Enter string:')
	s1=s.split(' ')
	c=0
	for i in range(len(s1)):
		if s1[i]==ss:
			c+=1
	return c
play_58()
