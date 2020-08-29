if __name__ == "__main__":
    A, B, C = map(int, input().split())
    # pow(A를, B제곱[, C로 나눈 머지지]) | C는 optional
    print(pow(A, B, C))