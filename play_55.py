def play_55():
	s=input()
	l=s.split(' ')
	s1,s2=l[0],l[1]
	i=0
	a=''
	b='\0'
	while(i<len(s1)):
		if ord(s1[i]) in range(65,91):
			q=ord(s1[i])+32
			a=chr(q)
		if ord(s2[i]) in range(65,91):
			q=ord(s2[i])+32
			b=chr(q)
		if s1[i]==s2[i] or a==s2[i] or b==s1[i]:
			i+=1
		else :
			return 'No'
	return "yes"
play_55()
