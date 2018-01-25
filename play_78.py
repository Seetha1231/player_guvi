def play_78():
	n=int(input('Enter n:'))
	l,k,res=[],[],[]
	print('Enter elements :')
	for i in range(n):
		l.append(int(input()))
	m=int(input('Enter m:'))
	print('Enter elements :')
	for i in range(m):
		k.append(int(input()))
	l.append(9999)
	k.append(9999)
	i=j=0
	for a in range(0,n+m):
		if l[i]<=k[j]:
			res.append(l[i])
			i+=1
		else :
			res.append(k[j])
			j+=1
	print(res)
play_78()
