bars = input()

stack = []
cnt = 0

# '('를 막대기의 시작점으로 주고 '()' 이렇게 여는괄호와 닫는괄호가 연속으로 나오면 레이저로 취급한다.
for i in range(len(bars)):
    if bars[i] == '(':  # 현재 왼쪽 괄호이면 스택에 쌓고
        stack.append(bars[i])
    else:  # 현재 오른쪽 괄호일 경우
        if bars[i-1] == '(':  # 이전에 왼쪽 괄호 일 때 : () 이렇게 되면 레이저 이므로
            stack.pop()  # 막대기의 시작점일거라 예상했던 '('를 하나 빼주고
            cnt += len(stack)  # 막대기가 담겨있는 stack 의 길이만큼 더해준다.
        elif bars[i-1] == ')':  # 이전에 오른쪽 괄호 일 때:
            stack.pop()  # 막대기의 끝부분이므로 '('를 하나 빼주고
            cnt += 1  # 막대기 하나가 끝났으므로 1을 더해준다.

print(cnt)
