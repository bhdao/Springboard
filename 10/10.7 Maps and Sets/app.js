// What does the following code return?
// new Set([1,1,2,2,3,4])
// It returns a set of {1, 2, 3, 4}

//What does the following code return?
//[...new Set("referee")].join("")
//It returns a string of "ref"

//What does the Map m look like after running the following code?
// let m = new Map();
// m.set([1,2,3], true);
// m.set([1,2,3], false);
//It looks like the following:
// 
//  0: {[1,2,3], true)}
//  1: {[1,2,3], false)}
// 

let thing = new Map();
thing.set([1, 2, 3], true);
thing.set([1, 2, 3], false);
console.log(thing.get([1, 2, 3]));

const hasDuplicate = (inputArr) => {
  let initialLength = inputArr.length;
  let removeDupes = new Set([...inputArr]);
  if (removeDupes.size !== initialLength) {
    return true
  } else { return false };
}

console.log(
  hasDuplicate([1, 3, 5, 1,]),
  hasDuplicate([1, 3, 5, -1,])
);

const vowelCount = (inputString) => {
  let vowels = "aeiou";
  let vowelMap = new Map();
  let lowerString = inputString.toLowerCase();
  for (const letter of lowerString) {
    if (vowels.includes(letter)) {
      if (vowelMap.has(letter)) {
        vowelMap.set(`${letter}`, vowelMap.get(`${letter}`) + 1);
      } else {
        vowelMap.set(`${letter}`, 0);
      }
    }
  }
  return vowelMap;
}