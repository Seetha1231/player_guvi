def play_93():
	n=int(input('Enter n:'))
	l,c=[],0
	print('Enter elements :')
	for i in range(n):
		l.append(int(input()))
	for i in range(n-1):
		for j in range(i+1,n):
			t=l[i]
			l[i]=l[j]
			l[j]=t
			break
	print(*l)
play_93()
