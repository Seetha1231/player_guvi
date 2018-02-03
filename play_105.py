 def play_105():
	n=int(input())
	l=list(map(int,input().split()))
	d={}
	for i in range(n):
		d[l[i]]=i
	for i in range(n):
		p=i
		for j in range(i+1,n):
			if l[p]>l[j]:
				p=j
		if p!=i:
			t=l[i]
			l[i]=l[p]
			l[p]=t
		print(d[l[i]]+1,end="\t")
    
play_105()
