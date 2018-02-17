def main():
    n=int(input())
    l=list(map(int,input().split()))
    s,k=0,1
    ss,sum=[],0
    for i in range(n):
        sum+=l[i]
    ss.append(sum)
    for j in range(1,n):
        sum=sum-l[j]
        ss.append(sum)
    for i in range(n):
        print(ss[i],end="\t")


if __name__ == '__main__':
    main()
