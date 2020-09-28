from collections import deque

if __name__ == "__main__":
    for tc in range(int(input())):
        N, M = map(int, input().split())  # 문서의 수, 몇번째로 인쇄될지 궁금한 문서의 인덱스
        documents = list(map(int, input().split()))
        index = deque([x for x in range(N)])
        documents = deque(documents)

        cnt = 0
        while documents:
            c = documents.popleft()
            i = index.popleft()
            if len(documents) == 0:
                print(cnt + 1)
                break
            if max(documents) > c:
                documents.append(c)
                index.append(i)
            else:
                cnt += 1

                if i == M:
                    print(cnt)
                    break
