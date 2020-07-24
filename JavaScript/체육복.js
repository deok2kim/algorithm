function solution(n, lost, reserve) {  
  const noDupleLost = lost.filter( (s) => (reserve.indexOf(s) === -1))
  const noDupleReserve = reserve.filter( (s) => (lost.indexOf(s) === -1))
  
  noDupleLost.sort()
  var answer = n-noDupleLost.length
  noDupleLost.forEach(lostStudent => {

    if (noDupleReserve.indexOf(lostStudent-1) >= 0) {
      answer ++

    } else if (noDupleReserve.indexOf(lostStudent+1) >= 0) {
        answer ++
        var reserveStudent = noDupleReserve.indexOf(lostStudent+1)
        noDupleReserve.splice(reserveStudent, 1)
    }
  })
  return answer;
}

console.log(solution(5, [2,5], [1,3,5]));
console.log(solution(5, [2,4], [3]));
console.log(solution(3, [3], 	[1]));

console.log(solution(5, [2,3], [3,4]))