def play_63():
	n=int(input('Enter n:'))
	l,m=[],[]
	print('Enter elements-1 :')
	for i in range(n):
		l.append(int(input()))
	print('Enter elements-2 :')
	for i in range(n):
		m.append(int(input()))
	for i in range(n):
		if l[i]==m[i]:
			print(l[i],end=" ")
play_63()
