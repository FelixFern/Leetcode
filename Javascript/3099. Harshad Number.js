/**
 * @param {number} x
 * @return {number}
 */
var sumOfTheDigitsOfHarshadNumber = function (x) {
  const sums = x
    .toString()
    .split("")
    .reduce((p, c) => parseInt(c) + p, 0);
  return x % sums === 0 ? sums : -1;
};
