def input():
    return f.readline().strip()
f = open('C:\\Users/113938/Desktop/swea/sample_input.txt')



for tc in range(int(input())):
    print(f'#{tc+1}', end=' ')
    N = int(input())
    value = round(pow(N, 1/3),2)
    if int(value) == value:
        print(int(value))
    else:
        print(-1)
    
