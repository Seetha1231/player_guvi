def play_75():
	n=int(input('Enter n:'))
	l,c=[],0
	print('Enter elements :')
	for i in range(n):
		l.append(int(input()))
	for i in range(n-1):
		for j in range(i+1,n):
			if l[i]<l[j]:
				c+=1
	print(c)
play_75()
