def play_39():
	n=int(input('Enter n :'))
	i=n
	while(i>1):
		i=n%2
		n//=2
	print(i==0)
play_39()
