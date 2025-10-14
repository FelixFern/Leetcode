/**
 * @param {number[]} nums
 * @param {number} k
 * @return {boolean}
 */
var hasIncreasingSubarrays = function (nums, k) {
  if (k === 1 && nums.length >= 2) return true;

  let prevIncreasing = -1;
  let curr = 1;

  for (let i = 0; i < nums.length - 1; i++) {
    if (nums[i] < nums[i + 1]) curr += 1;
    else {
      prevIncreasing = curr;
      curr = 1;
    }
    if (
      (prevIncreasing >= k && curr >= k) ||
      prevIncreasing >= 2 * k ||
      curr >= 2 * k
    )
      return true;
  }

  return false;
};
