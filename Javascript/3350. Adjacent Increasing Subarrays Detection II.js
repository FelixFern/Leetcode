/**
 * @param {number[]} nums
 * @return {number}
 */
var maxIncreasingSubarrays = function (nums) {
  let resMax = 1;
  let curr = 1;
  let prev = -1;

  const n = nums.length;

  for (let i = 0; i < n - 1; i++) {
    if (nums[i] < nums[i + 1]) {
      curr++;
    } else {
      if (Math.min(curr, prev) > resMax) resMax = Math.min(curr, prev);
      if (Math.floor(Math.max(curr, prev) / 2) > resMax)
        resMax = Math.floor(Math.max(curr, prev) / 2);
      prev = curr;
      curr = 1;
    }
  }

  if (Math.min(curr, prev) > resMax) resMax = Math.min(curr, prev);
  if (Math.floor(Math.max(curr, prev) / 2) > resMax)
    resMax = Math.floor(Math.max(curr, prev) / 2);

  return resMax;
};
