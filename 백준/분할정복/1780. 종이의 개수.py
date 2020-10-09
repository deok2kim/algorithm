from itertools import chain  # 2차원 리스트를 1차원리스트로 바꿔주는 친구


def bt(paper):
    global a, b, c
    nn = len(paper)

    if len(set(chain.from_iterable(paper))) == 1:
        if paper[0][0] == -1:
            a += 1
        elif paper[0][0] == 0:
            b += 1
        else:
            c += 1
    else:
        if nn != 3:
            for i in range(0, nn, nn // 3):
                for j in range(0, nn, nn // 3):
                    tmp_paper = [row[j:j + nn // 3] for row in paper[i:i + nn // 3]]
                    bt(tmp_paper)
        else:
            for i in range(nn):
                for j in range(nn):
                    if paper[i][j] == -1:
                        a += 1
                    elif paper[i][j] == 0:
                        b += 1
                    else:
                        c += 1


n = int(input())
papers = [list(map(int, input().split())) for _ in range(n)]
a, b, c = 0, 0, 0
bt(papers)
print(f'{a}\n{b}\n{c}')
