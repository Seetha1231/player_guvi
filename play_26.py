def play_26():
	text=input()
	ans=""
	prev=" "
	for i in text :
		if not (prev==" " and i==prev ):
			ans+=i
		prev=i
	print(ans)
  
play_26()
