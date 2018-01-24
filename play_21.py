 def play_21():
	x,y=[],[]
	for i in range(3):
		x.append(int(input('Enter x'+str(i))))
		y.append(int(input('Enter y'+str(i))))
	if ((y[1]-y[0]) * (x[2]-x[1])) == ((y[2]-y[1]) * (x[1]-x[0])) :
		print ('Yes')
	else :
		print('No')
play_21()
