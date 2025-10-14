/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isSubsequence = function (s, t) {
  let pt = 0;
  let found = 0;
  for (let i = 0; i < s.length; i++) {
    while (s[i] !== t[pt] && pt < t.length - 1) {
      pt++;
    }
    if (s[i] === t[pt]) {
      pt++;
      found++;
    }
  }
  return found === s.length;
};
