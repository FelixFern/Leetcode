/**
 * Forward declaration of guess API.
 * @param {number} num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 * var guess = function(num) {}
 */

/**
 * @param {number} n
 * @return {number}
 */
var guessNumber = function (n) {
  if (n === 1) return 1;

  let lp = 1;
  let rp = n;
  let mid = Math.floor((rp - lp) / 2);

  while (lp <= rp) {
    const temp = guess(mid);
    if (temp === 0) return mid;
    else if (temp === 1) {
      lp = mid + 1;
    } else {
      rp = mid - 1;
    }
    mid = lp + Math.floor((rp - lp) / 2);
  }
};
