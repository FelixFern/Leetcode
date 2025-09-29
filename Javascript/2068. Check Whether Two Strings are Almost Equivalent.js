/**
 * @param {string} word1
 * @param {string} word2
 * @return {boolean}
 */
var checkAlmostEquivalent = function (word1, word2) {
  const word1Freq = new Array(26).fill(0);
  const word2Freq = new Array(26).fill(0);

  word1.split("").forEach((a) => {
    word1Freq[a.charCodeAt(0) - "a".charCodeAt(0)] += 1;
  });
  word2.split("").forEach((a) => {
    word2Freq[a.charCodeAt(0) - "a".charCodeAt(0)] += 1;
  });

  let isValid = true;

  for (let i = 0; i < 26; i++) {
    const diff = Math.abs(word1Freq[i] - word2Freq[i]);
    if (diff > 3) isValid = false;
  }

  return isValid;
};
