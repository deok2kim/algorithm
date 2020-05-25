N = int(input())
M = int(input())

# 문제에서 M 의 범위가 0부터 이므로 M이 1이상이어야만 input을 받을 수 있다.
if M:
    broken = input().split()
else:
    broken = []

# 숫자 버튼을 눌러 갈 수 있는 채널을 넣을 리스트
channels = []
current_channel = 100
result = abs(N-current_channel)  # +,- 만 써서 N에 갈 수 있는 횟수 (이게 최소가 될 수 있다)
result_channel = 100
# ~1000000 까지 for문을 돌리며 고장난 숫자가 채널에 포함되어있지 않을 때만 채널리스트에 추가해준다.
for i in range(1000000):
    for j in str(i):
        # 고장난 키를 눌렀는가
        if j in broken:
            break

    else:
        channels.append(i)
        # 숫자 버튼을 눌러 갈 수 있는 채널과 내가 원하는 채널의 차이의 최솟값을 구해준다.
        if abs(N-i) < result:
            result = abs(N-i)
            result_channel = i

result = min(result+len(str(result_channel)), abs(N-current_channel))
print(result)
