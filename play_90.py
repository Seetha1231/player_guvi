def fact(n):
	f=1
	for i in range(1,n+1):
		f*=i
	return f
def play_90():
	n=int(input('Enter n:'))
	r=int(input('Enter r:'))
	ans=fact(n)/(fact(r)*fact(n-r))
	print(round(ans,1))
play_90()
