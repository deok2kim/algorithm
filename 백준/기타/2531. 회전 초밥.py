import sys

if __name__ == "__main__":
    N, d, k, c = map(int, sys.stdin.readline().split())
    sushi = [int(input()) for _ in range(N)]
    # 원형으로 연결된 경우이므로 앞부분의 k-1개 만큼의 초밥을 뒤에 추가해준다.
    sushi += sushi[:k-1]

    answer = 0
    for i in range(N):
        my_sushi = set(sushi[i:i+k])
        my_sushi.add(c)
        answer = max(answer, len(my_sushi))

    print(answer)


