def play_72():
	n=int(input('Enter n:'))
	l,max=[],-1
	print('Enter elements :')
	for i in range(n):
		l.append(int(input()))
	for i in range(n-1):
		for j in range(i+1,n):
			if l[i]<l[j]:
				break
			else :
				if l[i]>l[j]:
					if max<l[i]:
						max=l[i]
				break
	print(max)
play_72()
