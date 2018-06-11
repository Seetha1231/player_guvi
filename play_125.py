def gcd(l):
	for i in range(1,min(l)+1):
		f=0
		for j in l:
			if (j%i)!=0:
				f=1
				break
		if f!=1:
			val=i
	print(val)
gcd(list(map(int,input().split())))
