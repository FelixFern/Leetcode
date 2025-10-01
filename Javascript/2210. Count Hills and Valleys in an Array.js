/**
 * @param {number[]} nums
 * @return {number}
 */
var countHillValley = function (nums) {
  let res = 0;
  nums = nums.reduce((p, c) => {
    if (p[p.length - 1] === c) return [...p];
    return [...p, c];
  }, []);
  for (let i = 1; i < nums.length - 1; i++) {
    if (nums[i] > nums[i - 1] && nums[i] > nums[i + 1]) res += 1;
    if (nums[i] < nums[i - 1] && nums[i] < nums[i + 1]) res += 1;
  }

  return res;
};
