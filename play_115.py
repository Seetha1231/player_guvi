def main():
    l1,l2=(map(str,input().split()))
    l=[]
    if l1!=l2:
        for i in range(len(l1)-1):
            l.append(l1[i])
        l.append(l2)
    elif l1==l2:
        l.append(l1)
        l.append(l2)
    for i in l:
        print(i,end="")
if __name__ == '__main__':
    main()
