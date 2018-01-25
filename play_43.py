def play_43():
	n=int(input('Enter n :'))
	l=[]
	for i in range(n):
		l.append(int(input()))
	for i in range(n-1):
		for j in range(i+1,n):
			if l[i]<l[j]:
				continue
			return "no"
	return "Yes"
play_43()
