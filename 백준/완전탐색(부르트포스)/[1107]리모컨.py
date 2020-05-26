N = int(input())
M = int(input())

# 문제에서 M 의 범위가 0부터 이므로 M이 1이상이어야만 input을 받을 수 있다.
if M:
    broken = input().split()
else:
    broken = []

current_channel = 100
result = float['inf']
result_channel = 100
# ~1000000 까지 for문을 돌리며 고장난 숫자가 채널에 포함되어있지 않을 때만 채널리스트에 추가해준다.
for i in range(1000000):
    for j in str(i):
        # 고장난 키를 눌렀는가
        if j in broken:
            break

    else:
        # 숫자 버튼을 눌러 갈 수 있는 채널과 내가 원하는 채널의 차이의 최솟값을 구해준다.
        if abs(N-i) < result:
            result = abs(N-i)
            result_channel = i

# result: 숫자 버튼만 눌러 갈 수 있는 채널 중에서 현재(100)채널과 차이의 절대값이 최소일 때의 차이값
# len(str(result_channel)): 채널에 갈 때 눌러야 하는 숫자버튼의 갯수

# abs(N-current_channel): 오직 +,-로만 갈 때 눌러야하는 버튼 횟수 (이게 최소가 될 수 있다)
result = min(result+len(str(result_channel)), abs(N-current_channel))
print(result)
