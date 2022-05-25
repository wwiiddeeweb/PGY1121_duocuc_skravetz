var myArray = [1, 2, 2, 4, 5, 6, 7, 8, 8, 8];

function findMostFrequent(arr) {
  const reducer = arr.reduce((obj, val) => {
    if (!obj.hasOwnProperty(val)) {
      obj[val] = 1;
    } else {
      obj[val] += 1;
    }

    return obj;
  }, {});
  const longest = Math.max(...Object.values(reducer));
  const number = Object.keys(reducer).find((key) => reducer[key] == longest);
  return `Longest: ${longest}
Number: ${number}`;
}

console.log(findMostFrequent(myArray));
