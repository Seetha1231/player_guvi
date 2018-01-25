def play_61():
	n=int(input('Enter n:'))
	l=[]
	print('Enter elements :')
	for i in range(n):
		l.append(int(input()))
	k=int(input('Enter k:'))
	for i in range(n):
	      for j in range(i+1,n):
		      if l[i]+l[j]==k:
			      return 'yes'
	return 'no'
play_61()
