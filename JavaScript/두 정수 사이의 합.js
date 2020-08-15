function solution(a, b) {
  var answer = 0;
  if (a > b) {
    let tmp = a
    a = b
    b = tmp
  }
  for (let n = a; n <= b; n++) {
    answer += n
    
  }
  return answer;
}

console.log(solution(3, 5))
console.log(solution(3, 3))
console.log(solution(5, 3))