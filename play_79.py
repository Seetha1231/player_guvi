def play_79():
	n=int(input('Enter n:'))
	l,max=[],-1
	print('Enter elements :')
	for i in range(n):
		l.append(int(input()))
	l.sort(reverse=True)
	for i in range(n):
		for j in range(i+1,n):
			d=l[i]-l[j]
			if max<d:
				max=d
	print(max)
play_79()
