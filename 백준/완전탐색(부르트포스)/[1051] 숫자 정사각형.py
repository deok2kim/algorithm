def find_squre(s):
    # 정사각형의 꼭지점의 숫자 크기가 같은 경우를 찾는다.
    for i in range(n-s+1):
        for j in range(m-s+1):
            if numbers[i][j] == numbers[i][j+s-1] == numbers[i+s-1][j] == numbers[i+s-1][j+s-1]:
                return True

    return False


n, m = map(int, input().split())
numbers = [list(map(int, list(input()))) for _ in range(n)]

# size: 정사각형을 만들 수 있는 최대 크기
# size = m if n > m else size = n
if n > m:
    size = m
else:
    size = n

# 최대 크기부터 하나씩 줄여가며 시작
for k in range(size, 0, -1):
    # 네 꼭지점의 크기가 같은 정사각형을 찾았으면 True를 받아 넓이를 출력해주고 break
    if find_squre(k):
        print(k**2)
        break
