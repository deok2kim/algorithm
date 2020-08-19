// var arr = [1,2,3,4,5]

// a = arr.pop()
// console.log(arr) // [ 1, 2, 3, 4 ]
// console.log(a)
// arr.shift()

// console.log(arr) // [ 2, 3, 4 ]

function printAgeGroup(age) {
  var answer = "";
  var ageGroup = Math.floor(age / 10);
  if (ageGroup == 0) {
    answer = "10대 미만";
  } else if (ageGroup > 9) {
    answer = "90대 이상";
  } else {
    answer = `${ageGroup}0대`;
  }
  return answer;
}

for (let i = 0; i < 121; i++) {
  console.log(printAgeGroup(i));
}
