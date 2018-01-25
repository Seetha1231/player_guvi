def play_42():
	s=input('Enter string :')
	ss=input('Enter substring :')
	for i in range(len(s)):
		if ss==s[i:len(ss)+i]:
			return "yes"
	return "no"
play_42()
