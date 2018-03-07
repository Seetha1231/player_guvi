def main():
    n=int(input())
    l=list(map(int,input().split()))
    nn=len(l)
    c=1
    ll=[]
    if nn!=n:
        return 'Invalid'
    d={}
    for i in range(n):
        p=i
        for j in range(i+1,n):
            if l[i]==l[j]:
                c+=1
                p=j
        if l[i] not in d:
            d[l[i]]=c
        c=1
    for i in d:
        pos=i
        for j in d:
            if d[i]<=d[j]:
                pos=i
                if d[i]==d[j]:
                    if i>j:
                        pos=i
                    else :
                        pos=j
                    break
        ll.append(pos)
    for i in ll:
        print(i,end="\t")
if __name__ == '__main__':
    main()
