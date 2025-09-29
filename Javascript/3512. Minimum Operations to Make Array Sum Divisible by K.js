/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var minOperations = function (nums, k) {
  const sum = nums.reduce((p, c) => p + c, 0);
  return sum % k === 0 ? 0 : sum - Math.floor(sum / k) * k;
};
