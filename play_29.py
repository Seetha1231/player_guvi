def play_29():
	c=0
	s=int(input('Enter l :'))
	e=int(input('Enter r :'))
	for i in range(s,e+1):
		n=int(i**(0.5))
		if(i==n*n):
			c+=1
	print(c)
play_29()
