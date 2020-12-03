for tc in range(int(input())):
    p, q = map(float, input().split())  # p: 올바론 면으로 USB를 꽂을 확률, q: 정상적으로 USB가 꽂힐 확률

    # 1번 뒤집어서 올바른 면으로 꽂고 작동할 확률
    # 처음에 뒤집어서 꽂고 다음에 제대로 꽂는다
    s1 = (1 - p) * q

    # 2번 뒤집어서 올바른 면으로 꽂고 작동할 확률
    # 처음에 올바른 면 & 비정상 꽂기, 그다음 뒤집은 면(생략 - 저절로 된다), 마지막 제대로 꽂기
    s2 = p * (1 - q) * q
    print(f'#{tc + 1}', "YES" if s2 > s1 else "NO")
