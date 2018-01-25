def play_45():
	p=int(input('Enter p :'))
	a=int(input('Enter A :'))
	s=int(a**0.5)
	if float(s)==float(a**0.5):
		if int(a**(0.5))==(p//4) :
			return('Yes')
	return('No')
play_45()
