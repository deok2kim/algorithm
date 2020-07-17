from itertools import permutations


def solution(expression):
    answer = 0

    # 주어진 수식 숫자와 연산자로 분리하기
    sep_expression = []
    tmp = ''
    for i in range(len(expression)):
        if expression[i].isdecimal():  # 숫자라면 tmp 에 계속 더해주고
            tmp += expression[i]
        else:  # 연산자가 나올경우 list 에 숫자와 연산자를 각각 추가 해준다.
            sep_expression.append(tmp)
            tmp = ''
            sep_expression.append(expression[i])
    else:
        sep_expression.append(tmp)  # 마지막 숫자 추가

    # 계산하기
    operators = ['+', '-', '*']
    for ordered_operator in permutations(operators, 3):  # 퍼뮤테이션 함수를 이용해 연산자 3가지에 대한 순열을 생성
        copy_expression = sep_expression[:]  # 여러번 계산해야 하므로 복사해서 사용한다.
        for operator in ordered_operator:
            idx = 0  # 연산자를 하나씩 가져와서
            while idx < len(copy_expression):
                if copy_expression[idx] == operator:  # 연산해준다.
                    if operator == '-':
                        cal = int(copy_expression[idx-1]) - int(copy_expression[idx+1])
                    elif operator == '+':
                        cal = int(copy_expression[idx-1]) + int(copy_expression[idx+1])
                    else:
                        cal = int(copy_expression[idx-1]) * int(copy_expression[idx+1])

                    copy_expression = copy_expression[:idx-1] + list(str(cal).split()) + copy_expression[idx+2:]  # 계산 한 후 계산값을 배열에 넣어준다.

                else:
                    idx += 1

        else:
            answer = max(answer, abs(int(copy_expression[0])))  # 답은 절대값을 씌웠을 때 가장 큰 값

    return answer


print(solution("100-200*300-500+20"))  # 60420
print(solution("50*6-3*2"))  # 300