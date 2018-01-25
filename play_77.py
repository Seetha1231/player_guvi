def play_77():
	n=int(input('Enter n:'))
	l=[]
	print('Enter elements :')
	for i in range(n):
		l.append(int(input()))
	for i in range(n-1):
		for j in range(i+1,n):
			if l[i]<l[j]:
				m=l[j]
			break
	print(m)
play_77()
