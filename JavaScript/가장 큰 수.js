function solution(numbers) {
    var answer = '';
    numbers.sort((a, b) => {
        return (b + '' + a) * 1 - (a + '' + b) * 1
    })
    // console.log(numbers)
    answer = numbers.join('')
    return answer[0] == '0' ? '0' : answer;
}