def play_69():
	n=int(input('Enter n:'))
	l,c=[],0
	print('Enter elements :')
	for i in range(n):
		l.append(int(input()))
	k=int(input('Enter k:'))
	for i in range(n-k,n):
		l.pop()
	print(*l)
play_69()
