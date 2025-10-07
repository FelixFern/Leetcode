/**
 * @param {number[]} nums
 * @return {number}
 */
var longestSubarray = function (nums) {
  let lp = 0;
  let rp = 0;

  let totalOne = 0;
  let totalZero = 0;
  let maximum = 0;

  while (rp < nums.length) {
    if (nums[rp] === 1) totalOne++;
    else totalZero++;

    while (totalZero > 1) {
      if (nums[lp] === 1) totalOne--;
      else totalZero--;
      lp++;
    }

    maximum = Math.max(maximum, totalOne + totalZero - 1);
    rp++;
  }

  return maximum;
};
