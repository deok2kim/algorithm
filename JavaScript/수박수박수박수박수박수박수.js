function solution(n) {
    var answer = '';
    for (var i = 0; i < n; i++) {
        if (i % 2 == 0) answer += "수"
        else answer += "박"
    }
    return answer;
}