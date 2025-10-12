/**
 * @param {number[]} widths
 * @param {string} s
 * @return {number[]}
 */
var numberOfLines = function (widths, s) {
  let totalLine = 1;
  let curr = 0;

  for (alp of s) {
    const idx = alp.charCodeAt(0) - "a".charCodeAt(0);
    if (curr + widths[idx] > 100) {
      curr = 0;
      totalLine += 1;
    }
    curr += widths[idx];
  }

  return [totalLine, curr];
};
