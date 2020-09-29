import math

for tc in range(int(input())):
    x, y = map(int, input().split())
    dist = y - x  # 두 점 사이의 거리
    my_sqrt = int(math.sqrt(dist))  # 제곱근
    nmg = dist - my_sqrt ** 2  # 제곱까지 빼고 나머지
    cnt = my_sqrt * 2 - 1  # 제곱근 일때의 이동횟수
    if nmg == 0:
        print(cnt)
    elif nmg <= my_sqrt:
        print(cnt + 1)
    else:
        print(cnt + 2)
