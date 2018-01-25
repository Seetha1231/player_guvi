def play_98():
	n=int(input('Enter n:'))
	k=int(input('Enter k:'))
	kl=[i for i in range(k+1)]
	l=[]
	while(n!=0):
		s=n%10
		l.append(s)
		n//=10
	for i in l:
		if i in kl:
			continue
		else :
			return 'no'
	return 'yes'
play_98()
