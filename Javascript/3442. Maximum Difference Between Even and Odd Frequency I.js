/**
 * @param {string} s
 * @return {number}
 */
var maxDifference = function (s) {
  const odd = [];
  const even = [];

  const count = {};

  s.split("").forEach((val) => {
    count[val] = (count?.[val] ?? 0) + 1;
  });

  Object.values(count).forEach((val) => {
    if (val % 2 === 0) even.push(val);
    else odd.push(val);
  });

  return Math.max(...odd) - Math.min(...even);
};
