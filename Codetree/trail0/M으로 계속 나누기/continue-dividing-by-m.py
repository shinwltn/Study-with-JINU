N, M = map(int,input().split())

if all(2 <= x <= 1000000 for x in [N,M]):
    while N > 0 :
        print(N)
        N //= M