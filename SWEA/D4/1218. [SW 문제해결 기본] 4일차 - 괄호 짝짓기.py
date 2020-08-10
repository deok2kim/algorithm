def isRight(parenthesis):
    stack = []
    for paren in parenthesis:
        # 왼쪽 괄호
        if paren in parenthesis_list[0]:
            stack.append(paren)
        # 오른쪽 괄호
        else:
            if stack:
                k = stack[-1]
                for i in range(4):
                    # 괄호 네가지중 짝이 맞다면 통과
                    if k == parenthesis_list[0][i] and paren == parenthesis_list[1][i]:
                        stack.pop()
                        break
                # 아니라면 괄호 짝이 안맞는 것이므로 바로 0을 반환
                else:
                    return 0
    else:
        return 1


# 서로 맞는 괄호 짝을 체크하기 위한 리스트
parenthesis_list = [
    ['(', '{', '[', '<'],
    [')', '}', ']', '>']
]
for tc in range(1, 11):
    n = int(input())
    parenthesiss = input()

    answer = isRight(parenthesiss)
    print('#{} {}'.format(tc, answer))
