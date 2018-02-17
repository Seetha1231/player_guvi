def main():
    n=int(input())
    l=list(map(int,input().split()))
    s,k=0,0
    ss,sum=[],0
    for i in l:
        sum+=i
    for i in range(n):
        for c in range(i,i+1):
            s+=l[c]
        if i!=0:
            sum-=l[i]
        ss.append(s+sum)
    for i in range(n):
        print(ss[i],end="\t")
