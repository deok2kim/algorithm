if __name__ == '__main__':
    exp = input()

    # 한 번 마이너스가 나오면 뒤의 숫자는 전부 음수로 만들 수 있다.
    tmp = ''
    operator = '+'
    answer = 0
    # 마지막 값을 넣어주기 위해 아무 문자나 넣어준다
    exp += '_'
    for s in exp:
        if s.isdigit():
            tmp += s
        else:
            if operator == '+':
                answer += int(tmp)
                operator = s
            else:
                answer -= int(tmp)

            tmp = ''
    print(answer)
