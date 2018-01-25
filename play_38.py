def play_38():
	n=int(input('Enter n :'))
	l=[]
	for i in range(1,n//2+1):
		if n%i==0 and i%2==0:
			l.append(i)
	l.append(n)
	print(*l)
play_38()
