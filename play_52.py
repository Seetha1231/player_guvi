def play_52():
	n=int(input('Enter n:'))
	l=[]
	for i in range(n):
		l.append(int(input()))
	m1,m2=999,999
	k=int(input('Enter k:'))
	for j in range(k):
		m1=l[0]
		for i in range(1,len(l)):
			if m1>l[i]:
				m1=l[i]
		m2=m1

		if m2 in l:
			l.remove(m1)
	print(m2)
play_52()
