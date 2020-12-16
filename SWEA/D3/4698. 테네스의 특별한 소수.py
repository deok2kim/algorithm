
def input():
    return f.readline().strip()
f = open('C:\\Users/113938/Desktop/swea/4698. 테네스의 특별한 소수.txt')

N = 10**6
def set_prime():
    for i in range(N+1):
        if prime[i] == 1:
            for j in range(i*2, N+1, i):
                prime[j] = 0

prime = [1]*(N + 1)
prime[0], prime[1] = 0, 0
set_prime()

for tc in range(int(input())):
    D, A, B = map(int, input().split())
    answer = []
    for i in range(A, B+1):
        if str(D) in str(i) and prime[i]:
            answer.append(i)

    print(f'#{tc+1} {len(answer)}')