def play_41():
	n=int(input('Enter n :'))
	k=int(input('Enter k :'))
	i=n
	while(i>1):
		i=n%k
		n//=2
	print(i==0)
  
play_41()
