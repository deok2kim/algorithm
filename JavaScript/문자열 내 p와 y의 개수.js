function solution(s) {
    var answer = true;

    var pCnt = 0
    var yCnt = 0

    for (let i = 0; i < s.length; i++) {
        var lowerS = s[i].toLowerCase()
        if (lowerS == 'p') {
            pCnt++
        } else if (lowerS == 'y') {
            yCnt++
        }
    }

    if (pCnt != yCnt) {
        answer = false
    }

    return answer;
}