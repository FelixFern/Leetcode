/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function (nums) {
  nums.sort((a, b) => a - b);
  let res = [];

  for (let i = nums.length - 1; i >= 2; i--) {
    if (nums[i] === nums[i + 1]) continue;

    let left = 0;
    let right = i - 1;

    while (left < right) {
      const [a, b, c] = [nums[left], nums[right], nums[i]];

      const total = a + b + c;

      if (total === 0) {
        res.push([a, b, c]);
        left++;
        right--;

        while (left < right && nums[left] === nums[left - 1]) left++;
        while (left < right && nums[right] === nums[right + 1]) right--;
      } else {
        if (total < 0) left++;
        else right--;
      }
    }
  }

  return res;
};
