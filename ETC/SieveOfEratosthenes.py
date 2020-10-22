import math
import time


# 기본 소수 판별 알고리즘 O(N)
def prime(x):
    for i in range(2, x):
        if x % i == 0:
            return False

    return True


# O(N^(1/2))
def prime2(x):
    for i in range(2, int(math.sqrt(x))):
        if x % i == 0:
            return False

    return True


# 에라토스테네스의 체 O(n log log n)
def eratos(x):
    prime_number = [1] * (x + 1)
    for i in range(2, x):
        if prime_number[i] == 0:
            continue

        for j in range(i * 2, x + 1, i):
            prime_number[j] = 0


# 1부터 10000까지
n = 10000
print('기본')
start = time.time()
for k in range(2, n + 1):
    prime(k)
end = time.time()
print(f'시간: {end - start}')

print('제곱근')
start = time.time()
for k in range(2, n + 1):
    prime2(k)
end = time.time()
print(f'시간: {end - start}')

print('에라토스')
start = time.time()
eratos(n)
end = time.time()
print(f'시간: {end - start}')

'''
기본
시간: 0.3489978313446045
제곱근
시간: 0.012001991271972656
에라토스
시간: 0.0019986629486083984
'''
