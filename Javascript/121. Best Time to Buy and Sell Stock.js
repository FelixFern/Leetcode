/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function (prices) {
  let left = 0;
  let right = 1;

  let maxProfit = 0;

  while (left < prices.length - 1) {
    const [a, b] = [prices[left], prices[right]];
    if (right === prices.length) {
      left = right;
      right = left + 1;
    }
    if (b - a < 0) {
      left = right;
      right = left + 1;
    } else {
      if (b - a > maxProfit) maxProfit = b - a;
      right++;
    }
  }
  return maxProfit;
};
