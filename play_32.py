def play_32():
	n=int(input('Enter n:'))
	k=int(input('Enter k:'))
	l=[]
	for i in range(n):
		l.append(int(input('Enter no :')))
	if k in l:
		print('Yes')
	else :
		print('No')
play_32()
