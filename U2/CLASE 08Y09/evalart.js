myArray = [1, 2, 1, 3, 3, 1, 2, 1, 5, 1];

function histogram(arr = []) {
  contOne = 0;
  contTwo = 0;
  contThree = 0;
  contFour = 0;
  contFive = 0;
  for (const number of arr) {
    if (number === 1) {
      contOne += 1;
    } else if (number === 2) {
      contTwo += 1;
    } else if (number === 3) {
      contThree += 1;
    } else if (number === 4) {
      contFour += 1;
    } else if (number === 5) {
      contFive += 1;
    } else {
      return;
    }
  }
  msg = `1: ${"*".repeat(contOne)}
2: ${"*".repeat(contTwo)}
3: ${"*".repeat(contThree)}
4: ${"*".repeat(contFour)}
5: ${"*".repeat(contFive)}`;
  return msg;
}

console.log(histogram(myArray));
