 def play_25():
	n=int(input())
	l=[]
	for i in range(n):
		l.append(input('Enter :'))
	for i in range(n):
		p=i
		for j in range(i+1,n):
			if l[p]>l[j] and len(l[p])==len(l[j]):
				p=j
		print(p)
		if p!=i:
			t=l[i]
			l[i]=l[p]
			l[p]=t
	print(*l)
  
play_25()
