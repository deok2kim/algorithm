function solution(brown, yellow) {
    var answer = [];
    // 세로 길이를 3부터 하나씩 올려보자 - 그러면 가로 길이가 정해진다. 갈색
    // 전체 개수에서 2를 빼고 2로 나누면 최대 세로 개수
    for (let i = 3; i <= parseInt((brown - 2) / 2); i++) {
        // i 는 세로 길이
        // j 는 가로 길이
        let j = parseInt((brown - (i * 2) + 4) / 2)
        if ((i - 2) * (j - 2) == yellow) {
            answer = [j, i]
            break
        }
    }
    // 그리고 가로하나 세로하나 빼서 곱하면 노랑놈의 개수가 나온다
    return answer;
}