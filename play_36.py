def play_36():
	n=input('Enter n:')
	k=input('Enter k:')
	c=0
	for i in range(len(n)):
		if k in n[i]:
			c+=1
	print('Occurence :'+str(c))
play_36()
