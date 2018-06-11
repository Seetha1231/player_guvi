import math
n=int(input())
l=[]
for i in range(n):
	l.append(input())
min,word=math.inf,""
for i in l:
	if ord(i[0])<min:
		min=ord(i[0])
		word=i
print(word)
