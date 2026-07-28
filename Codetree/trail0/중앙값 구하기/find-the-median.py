A, B, C = map(int,input().split())

#A > B > C o
#A > C > B o
#B > A > C o
#B > C > A
#C > A > B o
#C > B > A o

if A > B :
    if A > C :
        if B > C :
            print(B)
        else :
            print(C)
    else :
        print(A)
elif A > C :
    print(A)
else :
    if C > B :
        print(B)
    else : 
        print(C)