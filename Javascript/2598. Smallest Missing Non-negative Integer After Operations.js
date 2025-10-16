/**
 * @param {number[]} nums
 * @param {number} value
 * @return {number}
 */
var findSmallestInteger = function (nums, value) {
  let count = {};

  for (num of nums) {
    let key = ((num % value) + value) % value;
    count[key] = (count[key] ?? 0) + 1;
  }
  let mex = 0;

  while (count[mex % value] > 0) {
    count[mex % value]--;
    mex += 1;
  }

  return mex;
};
