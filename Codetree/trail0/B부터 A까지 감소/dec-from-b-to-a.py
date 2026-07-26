A, B = map(int,input().split())

if 1 <= A <= B <= 100 :
    for i in range (B,A-1,-1):
        print(i, end=" ")