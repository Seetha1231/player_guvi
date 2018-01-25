 def play_44():
	s=input('Enter string :')
	k=int(input('Enter k :'))
	d=s[k:]
	d+=s[:k]
	print(d)
  
play_44()
