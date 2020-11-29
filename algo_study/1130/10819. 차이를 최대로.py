from itertools import permutations


def my_sum(numbers_tuple):  # 문제의 규칙에 맞게 더하기
    total = 0
    for i in range(N - 1):
        total += abs(numbers_tuple[i] - numbers_tuple[i + 1])

    return total


if __name__ == '__main__':
    N = int(input())
    numbers = list(map(int, input().split()))
    answer = 0
    for permu in permutations(numbers, N):  # N 이 적으므로 숫자를 배치할 수 있는 모든 경우의 수를 계산
        result = my_sum(permu)
        answer = max(answer, result)

    print(answer)
