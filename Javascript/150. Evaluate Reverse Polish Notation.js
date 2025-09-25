/**
 * @param {string[]} tokens
 * @return {parseInt}
 */
var evalRPN = function (tokens) {
  if (tokens.length <= 1) return parseInt(tokens[0]);

  const op = [];
  const nums = [];

  const operations = {
    "+": (a, b) => parseInt(a) + parseInt(b),
    "-": (a, b) => parseInt(a) - parseInt(b),
    "*": (a, b) => parseInt(a) * parseInt(b),
    "/": (a, b) => parseInt(a) / parseInt(b),
  };
  const operators = Object.keys(operations);

  while (tokens.length > 0 || op.length > 0) {
    if (nums.length >= 2 && op.length > 0) {
      const b = nums.pop();
      const a = nums.pop();
      const currOp = op.shift();
      nums.push(parseInt(operations[currOp](a, b)));
    }

    const curr = tokens.shift();
    if (!!curr) {
      console.log(curr);
      if (operators.includes(curr)) op.push(curr);
      else {
        nums.push(curr);
      }
    }
  }

  return nums[0];
};
