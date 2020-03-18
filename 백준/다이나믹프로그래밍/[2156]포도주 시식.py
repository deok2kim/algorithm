import sys

wine_list = []
result = 0
# n = int(input())
n = int(sys.stdin.readline())
for i in range(n):
    # wine_list.append(int(input()))
    wine_list.append(int(sys.stdin.readline()))

if len(wine_list) <= 2:
    result = sum(wine_list)
else:
    score = [wine_list[0], wine_list[0] + wine_list[1],
             max(wine_list[2] + wine_list[0],
                 wine_list[2] + wine_list[1],
                 wine_list[0] + wine_list[1])]
    for i in range(3, n):
        score.append(max(wine_list[i] + wine_list[i - 1] + score[i - 3],
                         wine_list[i] + score[i - 2],
                         score[i - 1]))

    result = score[-1]
    # print(wine_list)
    # print(score)

print(result)
