for tc in range(10):
    n = int(input())
    apt_list = list(map(int, input().split()))

    cnt = 0
    for i in range(2, n-2):
        around_top_apt = max(apt_list[i-2],apt_list[i-1],apt_list[i+1],apt_list[i+2])
        diff = apt_list[i] - around_top_apt
        if diff > 0:
            cnt += diff

    print('#{} {}'.format(tc+1, cnt))