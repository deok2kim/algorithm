T = int(input())
for test_case in range(1, 1 + T):
    s = input()
    day_list = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
    print(f'#{test_case} {7 - (day_list.index(s))}')
