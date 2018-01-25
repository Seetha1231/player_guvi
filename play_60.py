 def play_60():
	s=input('Enter string1 :')
	ss=input('Enter string2 :')
	for i in range(len(s)):
		if s[i]==ss[i]:
			return 'yes'
	return 'no'
play_60()
