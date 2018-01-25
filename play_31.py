def play_31():
	s=input()
	c1,c2=0,0
	for i in s:
		if i=='(':
			c1+=1
		if i==')':
			c2+=1
	if c1==c2:
		print('Yes')
	else :
		print('No')
play_31()
