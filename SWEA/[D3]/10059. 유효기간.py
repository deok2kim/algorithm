T = int(input())
for tc in range(1, T+1):
    n = input()
    MM = [i for i in range(1, 13)]
    result = ''
    for i in range(0, 4, 2):
        if int(n[i:i+2]) in MM:

            result += 'MM'
        else:
            result += 'YY'

    if result == 'MMYY' or result == 'YYMM':
        print(result)

    elif result == 'MMMM':
        print('AMBIGUOUS')

    else:
        print('NA')
