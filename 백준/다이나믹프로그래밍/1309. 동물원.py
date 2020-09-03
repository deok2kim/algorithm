if __name__ == "__main__":
    N = int(input())
    dp_no_lion = [0]*(N+1)  # 사자가 없을 때
    dp_left_lion = [0]*(N+1)  # 왼쪽에 사자가 있을 떄
    dp_right_lion = [0]*(N+1)  # 오른쪽에 사자가 있을 때

    dp_no_lion[0] = 1
    for i in range(1, N+1):
        dp_no_lion[i] = (dp_no_lion[i-1] + dp_left_lion[i-1] + dp_right_lion[i-1]) % 9901
        dp_left_lion[i] = (dp_no_lion[i-1] + dp_right_lion[i-1]) % 9901
        dp_right_lion[i] = (dp_no_lion[i-1] + dp_left_lion[i-1]) % 9901

    answer = dp_no_lion[N] + dp_left_lion[N] + dp_right_lion[N]
    print(answer % 9901)
