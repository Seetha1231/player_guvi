def play_51():
	n=int(input('Enter n:'))
	l=[]
	for i in range(n):
		l.append(int(input()))
	m1,m2=999,999
	for i in range(n):
		if m1>l[i]:
			m1=l[i]
		elif m2>l[i] and m1!=m2:
			m2=l[i]
	print('Second minimum :'+str(m2))
play_51()
