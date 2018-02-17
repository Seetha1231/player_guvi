def main():
    n=int(input())
    sum=0
    while(n!=0):
        r=n%10
        sum+=r*r
        n//=10
    print(sum)

if __name__ == '__main__':
    main()
