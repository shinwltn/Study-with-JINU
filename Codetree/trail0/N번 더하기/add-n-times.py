A, N = map(int,input().split())

if all (1 <= x <= 10 for x in [A,N]) :
 for i in range(N):
    A += N #기존 A에 N을 더한 뒤 그 결과를 다시 A에 저장
    print(A)
