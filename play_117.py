def main():
    s=input()
    l=list(s)
    ll=[]
    s=''
    for i in range(len(l)-1,-1,-1):
        l[i]+='-'
        s+=l[i]
    print(s)

if __name__ == '__main__':
    main()
