function solution(a, b) {
    var answer = '';
    var day = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    var days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    var today = b
    for (var i = 0; i < a; i++) {
        today += days[i]
    }
    console.log(today)
    answer = day[(today - 1) % 7]
    return answer;
}