def play_96():
	n=int(input('Enter number :'))
	s,l=0,[]
	while(n!=0):
		s=n%10
		l.append(s)
		n//=10
	print(l[0]+l[-1])
play_96()
