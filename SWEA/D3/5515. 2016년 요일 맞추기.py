T = int(input())
for t in range(1, T + 1):
    m, d = map(int, input().split())

    day_of_the_week = ['Fri', 'Sat', 'Sun', 'Mon', 'Tue', 'Wed', 'Thu']
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    for i in range(m - 1):
        d += month[i]

    result = (day_of_the_week.index(day_of_the_week[d % 7 - 1]) + 4) % 7
    print('#{} {}'.format(t, result))
