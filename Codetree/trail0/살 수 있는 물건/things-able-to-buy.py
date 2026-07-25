book = 3000
mask = 1000

N = int(input())

if N >= book :
    print("book")
elif mask <= N < book :
    print("mask")
else :
    print("no")