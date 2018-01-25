def play_40():
	n=int(input())
	c=0
	for i in range(n+1):
		for j in range(n+1):
			d=(i*1)+(j*2)
			if d==n:
				c+=1
	print(c)
play_40()
