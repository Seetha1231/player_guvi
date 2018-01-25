def play_65():
	n=int(input('Enter n:'))
	l=[]
	print('Enter elements :')
	for i in range(n):
		l.append(int(input()))
	for i in range(n):
		if l[i]<n:
			print(l[i],end=" ")
play_65()
