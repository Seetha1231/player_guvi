def main():
    n=int(input())
    f=0
    for i in range(2,n//2):
        if n%i==0 :
            for j in range(2,i//2+1):
                if  i%j==0:
                    f=1
                    break
            if f!=1:
                print(i)
            f=0



if __name__ == '__main__':
    main()
