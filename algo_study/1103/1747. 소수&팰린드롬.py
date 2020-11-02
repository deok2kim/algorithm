def make_eratos(l: int) -> list:
    eratos = [1] * (l + 1)
    eratos[0], eratos[1] = 0, 0
    for i in range(2, l):
        if eratos[i]:
            for j in range(i * 2, l, i):
                eratos[j] = 0
    return eratos


def is_palindrome(n: int) -> bool:
    s = str(n)
    if s == s[::-1]:
        return True
    return False


if __name__ == '__main__':
    N = int(input())

    # 100만이 넘어가는 첫 소수는 1003001
    limit = 1003001
    prime = make_eratos(limit)

    for num in range(N, limit + 1):
        # 1. 소수인지 판별한 후
        # 2. 팰린드롬인지 판별하기
        if prime[num] and is_palindrome(num):
            print(num)
            break
    else:
        print(1003001)
