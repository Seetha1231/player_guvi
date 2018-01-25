def play_100():
	n=int(input('Enter number :'))
	s,i,l=0,0,[]
	while(n!=0):
		s+=(n%10)*(2**i)
		i+=1
		n//=10
	while(s!=0):
		q=s%16
		s//=16
		l.append(q)
	for i in range(len(l)-1,-1,-1):
		print(l[i],end="")
play_100()
