/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var findMaxAverage = function (nums, k) {
  let maxSum = -1;
  let lp = 0;
  let rp = k - 1;
  let currSum = 0;

  for (let i = 0; i < k; i++) {
    currSum += nums[i];
    maxSum = currSum;
  }

  while (rp < nums.length - 1) {
    currSum -= nums[lp];
    lp++;
    rp++;
    currSum += nums[rp];
    console.log(currSum);
    maxSum = Math.max(currSum, maxSum);
  }

  return maxSum / k;
};
