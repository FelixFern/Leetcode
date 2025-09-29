/**
 * @param {string} s
 * @param {character} c
 * @return {number}
 */
var countSubstrings = function (s, c) {
  let count = 0;
  s.split("").forEach((val) => {
    if (val === c) count++;
  });
  return (count * (count + 1)) / 2;
};
