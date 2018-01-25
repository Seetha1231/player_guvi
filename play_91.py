def dtob():
	n=int(input('Enter number :'))
	l=[]
	while(n!=0):
		l.append(n%2)
		n//=2
	for i in range(len(l)-1,-1,-1):
		print(l[i],end="")
dtob()
