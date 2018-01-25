def play_76():
	n=int(input('Enter n:'))
	l,c1,c2=[],0,0
	print('Enter elements :')
	for i in range(n):
		l.append(int(input()))
	for i in range(n):
		if l[i]%2==0:
			c1+=1
			pos1=i
		else :
			c2+=1
			pos2=i
	if c1==n-1:
		print(l[pos2])
	elif c2==n-1:
		print(l[pos1])
play_76()
