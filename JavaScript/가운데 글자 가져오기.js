function solution(s) {
    var answer = '';
    const len = s.length
    if (len % 2 == 0) {
        answer = s.slice(parseInt(len/2)-1, parseInt(len/2)+1)
    } else {
        answer = s[parseInt(len / 2)]
    }

    return answer;
}

console.log(solution("abcde")) // c
console.log(solution("qwer")) // we