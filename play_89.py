 def play_89():
	n=int(input('Enter n:'))
	r=int(input('Enter r:'))
	ans=fact(n)/fact(n-r)
	print(round(ans,3))
play_89()
