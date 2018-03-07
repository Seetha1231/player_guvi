def main():
    s=input()
    l=list(s)
    ll=[]
    s=''
    for i in l:
        i+='-'
        s+=i
    print(s)

if __name__ == '__main__':
    main()
