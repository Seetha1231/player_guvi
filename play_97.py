def play_97():
	n=int(input('Enter l:'))
	m=int(input('Enter r:'))
	s=0
	for i in range(n,m+1):
		if i%2!=0:
			s+=i
	print(s)
play_97()
