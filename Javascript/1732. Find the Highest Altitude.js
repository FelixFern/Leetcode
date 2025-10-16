/**
 * @param {number[]} gain
 * @return {number}
 */
var largestAltitude = function (gain) {
  let prefixSum = Array(gain.length).fill(0);

  for (let i = 0; i < gain.length; i++) {
    if (i === 0) {
      prefixSum[i] = gain[i];
    } else {
      prefixSum[i] = prefixSum[i - 1] + gain[i];
    }
  }
  return Math.max(...prefixSum, 0);
};
