def play_71():
	n=int(input('Enter n:'))
	l,c=[],0
	print('Enter elements :')
	for i in range(n):
		l.append(int(input()))
	for i in range(n-1):
		for j in range(i+1,n):
			if l[i]>l[j]:
				print(l[i],end=' ')
			else :
				print(l[j],end=' ')
			break
play_71()
