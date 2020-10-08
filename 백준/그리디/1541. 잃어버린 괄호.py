c = input()
answer = 0
c += '*'
# 문제의 핵심!! 마이너스가 최초로 한번 나오는 순간 뒤의 모든 숫자들은 마이너스로 취급한다.!!!
number = ''
operator = '+'
for i in range(len(c)):
    if c[i].isdigit():
        number += c[i]
    else:
        if operator == '+':
            answer += int(number)
        else:
            answer -= int(number)

        if c[i] == '-':
            operator = '-'
        number = ''

print(answer)
