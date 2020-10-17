function solution(n) {
    var answer = 0;

    var numbers = []
    if (n < 3) {
        numbers.push(n)
    } else {
        var mok = 0
        var nmg = 0
        while (n >= 3) {
            console.log(n)
            mok = parseInt(n / 3)
            nmg = n % 3
            console.log(mok, nmg)
            n = mok
            numbers.push(nmg)
        }
        numbers.push(mok)
    }

    console.log(numbers)
    numbers.reverse()
    for (var i = 0; i < numbers.length; i++) {
        answer += numbers[i] * (3 ** i)
    }
    return answer;
}

console.log(solution(45))