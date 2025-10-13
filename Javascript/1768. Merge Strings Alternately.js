/**
 * @param {string} word1
 * @param {string} word2
 * @return {string}
 */
var mergeAlternately = function (word1, word2) {
  let res = "";
  const word1Splt = word1.split("");
  const word2Splt = word2.split("");

  while (word1Splt.length > 0 || word2Splt.length > 0) {
    const p1 = word1Splt.shift();
    const p2 = word2Splt.shift();

    if (p1) res += p1;
    if (p2) res += p2;
  }

  return res;
};
