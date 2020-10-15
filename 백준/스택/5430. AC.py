from collections import deque

for tc in range(int(input())):
    # RR이면 원래상태이므로 제거해줌
    order = input().replace('RR', '')

    n = int(input())
    number = input()[1:-1]
    if number:
        number = deque(list(map(int, number.split(','))))

    # R은 뒤집지 말고
    my_reverse = False
    for o in order:
        if o == 'R':
            my_reverse = not my_reverse
        elif o == 'D':
            if number:
                if my_reverse:
                    number.pop()
                else:
                    number.popleft()
            else:
                print('error')
                break
    else:
        number = list(number)
        if my_reverse:
            number = number[::-1]

        print(f'[{",".join(list(map(str, number)))}]')
