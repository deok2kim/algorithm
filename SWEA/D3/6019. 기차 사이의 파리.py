if __name__ == "__main__":
    T = int(input())
    for tc in range(1, 1 + T):
        # 사이의 거리, A 속력, B 속력, 파리 속력
        D, A, B, F = map(int, input().split())

        # s = v*t 파리가 날아간 거리
        fly_d = 0

        idx = 0
        while D >= 10**(-6):
            # 오른쪽 날아가기
            if idx % 2 == 0:
                d = (D * B * F) / (F * (B + F))
                fly_d += d

            # 왼쪽 날아가기
            else:
                d = (D * A * F) / (F * (A + F))
                fly_d += d
            t = d / F
            D -= (A + B) * t

        print(f'#{tc} {fly_d}')
