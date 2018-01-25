def play_35():
	s=input()
	l= l=s.split(' ')
	r,max,c=[],-1,0
	for i in l:
		for j in range(len(i)):
			for k in range(j+1,len(i)):
				if i[j]==i[k]:
					c+=1
			if max<c:
				max=c
				pos=j
			c=0
		print(i[pos],end="\t")
		max,c=-1,0
play_35()
