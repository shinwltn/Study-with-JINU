a, b, c = map(int, input().split())
sum = a+b+c
average = sum//3


if 1 <= a <= 100 and 1 <= b <= 100 and 1 <= c <= 100 :
    print(sum,f"{average}",(sum-average),sep='\n')

#inp = input()
#arr = inp.split()
#a = int(arr[0])
#b = int(arr[1])
#c = int(arr[2])

#print(a+b+c)
#print((a+b+c)//3)
#print((a+b+c) - (a+b+c)//3)