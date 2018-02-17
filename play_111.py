def main():
    n,m=map(int,(input().split()))
    ll=list(map(int,input().split()))
    for i in range(n):
        for j in range(n,m+n):
            if ll[i] == ll[j]:
                print(ll[i],end="\t")
                break



if __name__ == '__main__':
    main()
