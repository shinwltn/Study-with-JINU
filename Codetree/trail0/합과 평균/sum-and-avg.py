A, B = map(int,input().split())

sum = A+B
average = (A+B)/2

if 1 <= A <= 100 and 1 <= B <= 100 :
    print(f"{sum}",f"{average:.1f}")