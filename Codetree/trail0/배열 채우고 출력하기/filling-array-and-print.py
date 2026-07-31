#배열을 구현하여 주어진 수를 입력받기
arr = list(input().split())

# 9부터 0까지의 인덱스에 주어진 문자를 차례대로 출력
for i in range(9,-1,-1): #(시작값,끝값[꼭 숫자 \1\만큼 더 입력해야함],step)
    print(arr[i],end="")
