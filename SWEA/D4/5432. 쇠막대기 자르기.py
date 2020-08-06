from _collections import deque

for tc in range(1, 1+int(input())):
    iron_bar = input()
    q = deque()
    cnt = 0

    for i in range(len(iron_bar)):
        if iron_bar[i] == '(':
            q.append(iron_bar[i])
        elif iron_bar[i] == ')':
            if iron_bar[i-1] == '(':  # 레이저일 때
                q.pop()
                cnt += len(q)
                # print('자른다', cnt)

            else:  # 막대기 끝부분 일 때
                q.pop()
                cnt += 1
                # print('끝부분', cnt)

    print('#{} {}'.format(tc, cnt))
