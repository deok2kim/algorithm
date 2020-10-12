def is_right(s):
    stack = []
    for ss in s:
        if ss == '(':
            stack.append(ss)
        elif ss == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                return False
        elif ss == '[':
            stack.append(ss)
        elif ss == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                return False
    if stack:
        return False
    return True


def my_stack(s):
    stack = []
    for c in s:
        print(stack)

        if c == '(':
            stack.append(c)
        elif c == '[':
            stack.append(c)
        elif c == ')':
            tmp = 2
            while True:
                t = stack.pop()
                if type(t) == int:
                    tmp *= t
                elif t == '(':
                    stack.append(tmp)
                    break
        elif c == ']':
            tmp = 3
            while True:
                t = stack.pop()
                if type(t) == int:
                    tmp *= t
                elif t == '[':
                    stack.append(tmp)
                    break
        tmp = 0
        while stack:
            t = stack.pop()
            if type(t) == int:
                tmp += t
            else:
                stack.append(t)
                break
        if tmp:
            stack.append(tmp)


    return stack[-1]


S = input()
if is_right(S):
    print(my_stack(S))
else:
    print(0)
