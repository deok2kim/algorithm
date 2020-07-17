from itertools import permutations

def solution(expression):
    answer = 0

    # 주어진 수식 숫자와 연산자로 분리하기
    sep_expression = []
    tmp = ''
    for i in range(len(expression)):
        if expression[i].isdecimal():
            tmp += expression[i]
        else:
            sep_expression.append(tmp)
            tmp = ''
            sep_expression.append(expression[i])
    else:
        sep_expression.append(tmp)
    # print(sep_expression)

    #
    operators = ['+', '-', '*']
    for ordered_operator in permutations(operators, 3):
        copy_expression = sep_expression[:]
        for operator in ordered_operator:
            # print(operator)
            idx = 0
            while idx < len(copy_expression):
                if copy_expression[idx] == operator:
                    if operator == '-':
                        cal = int(copy_expression[idx-1]) - int(copy_expression[idx+1])
                    elif operator == '+':
                        cal = int(copy_expression[idx-1]) + int(copy_expression[idx+1])
                    else:
                        cal = int(copy_expression[idx-1]) * int(copy_expression[idx+1])

                    copy_expression = copy_expression[:idx-1] + list(str(cal).split()) + copy_expression[idx+2:]
                    # print(copy_expression)

                else:
                    idx += 1

        else:
            answer = max(answer, abs(int(copy_expression[0])))

    return answer


print(solution("100-200*300-500+20"))  # 60420
print(solution("50*6-3*2"))  # 300