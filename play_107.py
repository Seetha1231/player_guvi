def main():
    n=list(map(str,input().split()))
    x=input()
    pos=-1
    for i in range(len(n)):
        if n[i] in x:
            pos=i+1
    print(pos)

if __name__ == '__main__':
    main()
