function solution(numbers, target) {
    var answer = 0;
    const N = numbers.length

    function dfs(number, idx) {
        if (idx == N) {
            if (number == target) {
                answer++
            }
            return
        }
        dfs(number + numbers[idx], idx + 1)
        dfs(number - numbers[idx], idx + 1)
    }

    dfs(0, 0)
    return answer;
}