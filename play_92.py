 def play_92():
	n=int(input('Enter number :'))
	s,i=0,0
	while(n!=0):
		s+=(n%10)*(2**i)
		n//=10
		i+=1
	print(s)
play_92()
