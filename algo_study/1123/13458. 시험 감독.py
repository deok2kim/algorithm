import sys
import math

input = sys.stdin.readline

if __name__ == '__main__':
    N = int(input())  # 시험장의 개수
    A = list(map(int, input().split()))  # 각 시험장의 응시자 수
    B, C = map(int, input().split())  # B: 감독관이 감시할 수 있는 응시자 수, C: 부감독관이 감시할 수 있는 응시자 수

    answer = 0
    for number_of_students in A:
        answer += math.ceil((number_of_students - B if number_of_students > B else 0) / C) + 1

    print(answer)
