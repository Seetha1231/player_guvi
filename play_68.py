def play_68():
	n=int(input('Enter n:'))
	l,c,max=[],0,-1
	print('Enter elements :')
	for i in range(n):
		l.append(int(input()))
	for i in range(n):
		for j in range(i+1,n):
			if l[i]==l[j]:
				c+=1
		if max<c:
			max=c
		c=0
	print(max+1)
play_68()
