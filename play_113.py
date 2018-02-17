def main():
    n=list(map(int,(input().split('/'))))
    print(n[0]>=1 and n[1]>=1 and n[2]>=1 and (n[0]<=30 or n[0]<=31 or n[0]<=29) and (n[1]<=12))


if __name__ == '__main__':
    main()
