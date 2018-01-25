def play_64():
	n=int(input('Enter n:'))
	l=[]
	print('Enter elements :')
	for i in range(n):
		l.append(int(input()))
	k=int(input('Enter k:'))
	for i in range(n):
		if l[i]<k:
			print(l[i],end=" ")

play_64()
