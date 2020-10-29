for tc in range(int(input())):
    paren = input()
    stack = []
    for p in paren:
        if p == '(':
            stack.append(p)
        else:
            if not stack:
                print('NO')
                break
            else:
                stack.pop()
    else:
        if stack:
            print('NO')
        else:
            print('YES')
