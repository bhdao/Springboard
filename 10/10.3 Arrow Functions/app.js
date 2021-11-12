const double = (arr) => { return arr.map((val) => val * 2) };

const squareAndGetEvens = (nums) => {
  const squares = nums.map((num) => { return num ** 2 })
  const evens = squares.filter((square) => { return square % 2 === 0 });
  return evens;
}