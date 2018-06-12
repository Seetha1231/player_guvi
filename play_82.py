def play_82():
	n=int(input())
	l=list(map(int,input().split()))
	v=l[0]
	for i in range(1,n):
		v=v&l[i]
	print(v)
play_82()
