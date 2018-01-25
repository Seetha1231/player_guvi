def play_30():
	c=0
	l1=list(input('Enter string 1:'))
	l2=list(input('Enter string 2:'))
	for i in range(len(l1)):
		if l1[i]!=l2[i]:
			c+=1
	k=int(input('Enter k :'))
	if c==k:
		print('Yes')
	else :
		print('No')
    
play_30()
