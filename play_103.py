def main():
    n=int(input())
    s=0
    l=list(map(int,input().split()))
    for i in range(n-1):
        for j in range(i,i+2):
            s+=l[i]
    print(s)

if __name__ == '__main__':
    main()
