for tc in range(1, 1 + int(input())):
    croak = input()

    # 울음소리를 카운팅할 딕셔너리
    croak_counting = {
        'c': 0,
        'r': 0,
        'o': 0,
        'a': 0,
        'k': 0,
    }
    answer = -1

    # 울음소리를 하나하나 순서대로 확인해준다.
    for s in croak:
        # 울음소리에 따라 카운트를 1씩 올려주고
        croak_counting[s] += 1
        # 다음 울음소리가 c가 나오고 croak가 완성된 상태라면 다음에 나온 c는 이전 울음소리의 반복이므로 전체 -1 해준다.
        if 0 not in croak_counting.values() and s == 'c':
            for ss in croak_counting.keys():
                croak_counting[ss] -= 1

        # 울음소리가 순서에 맞지 않게 나왔을 때
        if croak_counting['c'] < croak_counting['r']:
            break
        if croak_counting['r'] < croak_counting['o']:
            break
        if croak_counting['o'] < croak_counting['a']:
            break
        if croak_counting['a'] < croak_counting['k']:
            break

    # 딕셔너리에 들어간 울음소리의 수가 전체 개구리의 숫자이다
    if len(set(croak_counting.values())) == 1:
        answer = croak_counting['c']

    print('#{} {}'.format(tc, answer))
