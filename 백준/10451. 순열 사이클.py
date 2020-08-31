if __name__ == "__main__":
    for tc in range(1, 1+int(input())):
        N = int(input())
        numbers = list(map(int, input().split()))

        visited = [0]*(N+1)
        cnt = 0
        for i in range(1, N+1):
            if not visited[i]:
                visited[i] = 1
                stack = [i]
                while stack:
                    c = stack.pop()
                    if not visited[numbers[c-1]]:
                        stack.append(numbers[c-1])
                        visited[numbers[c-1]] = 1
                else:
                    cnt += 1

        print(cnt)