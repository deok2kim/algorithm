import math
n = int(input())
numbers = [int(input()) for _ in range(n)]
# print(numbers)
numbers.sort(reverse=True)

diff_numbers = []
for i in range(n-1):
    diff_numbers.append(numbers[i]-numbers[i+1])

tmp_gcd = 0
if len(diff_numbers) == 1:
    tmp_gcd = diff_numbers[0]
elif len(diff_numbers) == 2:
    tmp_gcd = math.gcd(diff_numbers[0], diff_numbers[1])
else:
    for i in range(len(diff_numbers)):
        if i == 0:
            tmp_gcd = diff_numbers[i]
        else:
            tmp_gcd = math.gcd(tmp_gcd, diff_numbers[i])

result = [tmp_gcd]
for i in range(2, int(math.sqrt(tmp_gcd))+1):
    if tmp_gcd % i == 0:
        result.append(i)
        result.append(tmp_gcd//i)

result = list(set(result))
result.sort()
print(' '.join(list(map(str, result))))
