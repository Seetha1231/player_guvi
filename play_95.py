def play_95():
	n=int(input('Enter number(N) :'))
	p=int(input('Enter number(P) :'))
	k=int(input('Enter number(K) :'))
	k+=p-1
	while(n!=0 and k!=0):
			s=n%10
			n//=10
			k-=1
	print(s)
play_95()
