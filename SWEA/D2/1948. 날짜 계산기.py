# T = int(input())
# for t in range(1, T+1):
#     sm, sd, em, ed = map(int, input().split())
#     month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     result = 1 + ed - sd
#     for i in range(sm, em):
#         result += month[i]
#     print('#{} {}'.format(t, result))


# datetime 사용법
import datetime
T = int(input())
for tc in range(1, T + 1):
    a1, a2, b1, b2 = map(int, input().split())
    a = datetime.datetime(2019,b1,b2) - datetime.datetime(2019,a1,a2)
    b = str(a).split(' ')[0]
    print('#{} {}'.format(tc, int(b)+1))
