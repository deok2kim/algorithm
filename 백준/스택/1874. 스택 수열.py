import sys

input = sys.stdin.readline

numbers = []
n = int(input())
for _ in range(n):
    numbers.append(int(input()))

stack = []
result = []
number = 1
idx = 0
while idx < n:
    if stack and stack[-1] == numbers[idx]:
        stack.pop()
        idx += 1
        result.append("-")
    elif number < n + 1:
        stack.append(number)
        result.append("+")
        number += 1
    else:
        break

if stack:
    print("NO")
else:
    for r in result:
        print(r)
