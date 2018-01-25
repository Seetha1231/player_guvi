def play_74():
	s=input('Enter string :')
	l=list(s)
	for i in range(len(l)):
		for j in range(i+1,len(l)):
			if l[i]==l[j]:
				return 'Yes'
	return 'No'
play_74()
