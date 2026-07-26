a, b = map(int,input().split())
c, d = map(int,input().split())


if 1 <= all(1<=x<=100 for x in [a,b,c,d]):
    if a>c and b>d  :
        print(1)
    else :
        print(0)
