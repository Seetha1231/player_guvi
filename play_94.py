def play_94():
	n=int(input('Enter number :'))
	s,l=0,[]
	while(n!=0):
		s=n%10
		if s in l:
			return "yes"
		l.append(s)
		n//=10
	return "no"
play_94()
