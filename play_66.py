def play_66():
	n=int(input('Enter n:'))
	l,c=[],0
	print('Enter elements :')
	for i in range(n):
		l.append(int(input()))
	k=int(input('Enter k:'))
	for i in range(n):
		for j in range(i+1,n):
			if l[i]==l[j]:
				c+=1
		if c==k-1:
			print(l[i],end=" ")
		c=0
play_66()
