def main():
    n=int(input())
    l=list(map(int,input().split()))
    s,c=0,0
    while(True):
        c+=1
        for i in l:
            if c%i==0:
                s+=1
                continue
            else:
                break
        if s==n:
            break
        s=0
    print(c)



if __name__ == '__main__':
    main()
