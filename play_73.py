def play_73():
	n=int(input('Enter n:'))
	l,max=[],-1
	print('Enter elements :')
	for i in range(n):
		l.append(int(input()))
	k=int(input('Enter k:'))
	for i in range(n):
		for j in range(i+1,n):
			if i==0:
				ans=l[i]-l[1]
			elif i==n-1:
				ans=l[i]-l[i-1]
			else :
				ans=l[i]-l[i-1]-l[i+1]
			if ans<0:
					ans=-ans
			if ans==k:
				return(l[i])
play_73()
