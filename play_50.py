def play_50():
	n=int(input('Enter n:'))
	for i in range(2,n//2):
		if n%i==0:
			return "yes"
	return "no"
  
play_50()
