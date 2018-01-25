def play_80():
	n=int(input('Enter n:'))
	l,min=[],9999
	print('Enter elements :')
	for i in range(n):
		l.append(int(input()))
	l.sort(reverse=True)
	for i in range(n):
		for j in range(i+1,n):
			d=l[i]-l[j]
			if min>d:
				min=d
	print(min)
play_80()
