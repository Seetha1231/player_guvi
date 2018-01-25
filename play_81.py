def play_81():
	n=int(input('Enter n:'))
	l,max=[],-1
	print('Enter elements :')
	for i in range(n):
		l.append(int(input()))
	for i in range(0,n-1,2):
		s=l[i]&l[i+1]
		if max<s:
			max=s
	print(max)
play_81()
