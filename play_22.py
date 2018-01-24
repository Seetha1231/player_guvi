def play_22():
	x=int(input())
	y=int(input())
	while(x!=y):
		if x>y:
			x-=y
		else :
			y-=x
	print(x)
play_22()
