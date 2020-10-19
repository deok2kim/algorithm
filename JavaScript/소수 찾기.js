function solution(n) {
    var answer = 0;
    let dp = Array(n + 1).fill(1)
    for (var i = 2; i < n + 1; i++) {
        if (dp[i] === 0) {
            continue
        }
        for (var j = i * 2; j < n + 1; j += i) {
            dp[j] = 0
        }
    }
    for (var i = 2; i < n + 1; i++) {
        answer += dp[i]
    }

    return answer;
}