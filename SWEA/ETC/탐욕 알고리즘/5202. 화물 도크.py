for tc in range(int(input())):
    n = int(input())  # 신청서
    work = [list(map(int, input().split())) for _ in range(n)]

    s_work = sorted(work, key=lambda x: x[1])
    print(s_work)
    print(work)
    work.sort()
    print(work)