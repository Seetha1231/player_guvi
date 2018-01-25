def play_59():
	n=int(input('Enter n:'))
	s,e='',''
	l=[]
	for i in range(n):
		l.append(int(input()))
	for i in range(n):
		if l[i]!=0:
			s+=str(l[i])+' '
		if l[i]==0:
			e+=s+' '
			s=''
	print(e)
play_59()
