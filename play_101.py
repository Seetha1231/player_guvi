def play_101():
	n=int(input('Enter number :'))
	l,max,s=[],-1,0
	print('Enter elements :')
	for i in range(n):
		l.append(int(input()))
	for i in range(n):
		for j in range(i+1,n):
			s+=l[j]
		if max<s:
			max=s
		s=0
	print(max)
play_101()
