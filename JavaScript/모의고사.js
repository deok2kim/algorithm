function solution(answers) {
  var answer = [];
  const student1 = [1,2,3,4,5]
  const student2 = [2,1,2,3,2,4,2,5]
  const student3 = [3,3,1,1,2,2,4,4,5,5]
  
  let student1Score = 0
  let student2Score = 0
  let student3Score = 0
  
  for(var i=0; i<answers.length; i++) {
      var a = i;
      if (i >= student1.length) {
          a = i % student1.length
      } 
      if (student1[a] == answers[i]) {
          student1Score ++
      }
      
      if (i >= student2.length) {
          a = i % student2.length
      } 
      
      if (student2[a] == answers[i]) {
          student2Score ++
      }
      
      if (i >= student3.length) {
          a = i % student3.length
      } 
      
      if (student3[a] == answers[i]) {
          student3Score ++
      }
  }
  const maxScore = Math.max(student1Score, student2Score, student3Score)
  if (student1Score == maxScore) {
      answer.push(1)
  }
  if (student2Score == maxScore) {
      answer.push(2)
  }
  if (student3Score == maxScore) {
      answer.push(3)
  }
  return answer;
}

console.log(solution([1,2,3,4,5]))
console.log(solution([1,3,2,4,2]))
console.log(solution([1,3,2,4,2,3,4]))