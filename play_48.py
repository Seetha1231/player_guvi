def play_48():
	n=int(input('Enter n:'))
	for i in range(2,n//2):
		if n%i==0 and i%2!=0:
			print(i,end="\t")
      
play_48()
