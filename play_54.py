 def play_54():
	s=input()
	l=s.split(' ')
	s1,s2=l[0],l[1]
	i=0
	while(i<len(s1)):
		if s1[i]==s2[i]:
			i+=1
		else :
			return 'No'
	return "yes"
play_54()
