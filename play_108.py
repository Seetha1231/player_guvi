def main():
    n=int(input())
    l=list(map(int,input().split()))
    s=0
    ss=[]
    for i in range(n):
        s+=l[i]
        ss.append(s)
    for i in range(len(ss)):
        print(ss[i],end="\t")


if __name__ == '__main__':
    main()
