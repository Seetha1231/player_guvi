def play_106():
	n=int(input())
	l=list(map(int,input().split()))
	d=[]
	for i in l:
		if i not in d:
			print(i,end=" ")
			d.append(i)
play_106()
