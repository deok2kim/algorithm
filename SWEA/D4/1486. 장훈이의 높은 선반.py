"""
1
5 16
1 3 3 5 6
"""

def power_set(idx, tot):
    global result

    if m <= tot:
        result = min(tot, result)
        return

    if idx == n:
        return

    # 선택 O
    power_set(idx+1, people[idx]+tot)

    # 선택 X
    power_set(idx+1, tot)


for tc in range(1, 1 + int(input())):
    n, m = map(int, input().split())
    people = list(map(int, input().split()))

    result = float('inf')
    power_set(0, 0)
    print('#{} {}'.format(tc, result-m))
