def play_104():
	n=int(input('Enter number :'))
	l,s=[],0
	print('Enter elements :')
	for i in range(n):
		l.append(int(input()))
	for i in range(0,n-1):
		s+=l[i]+l[i+1]
	print(s)
play_104()
