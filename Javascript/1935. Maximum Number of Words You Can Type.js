/**
 * @param {string} text
 * @param {string} brokenLetters
 * @return {number}
 */
var canBeTypedWords = function (text, brokenLetters) {
  let count = 0;
  const splitted = text.split(" ");
  const brokenLettersSplitted = brokenLetters.split("");

  splitted.forEach((v) => {
    if (brokenLettersSplitted.map((j) => !v.includes(j)).every(Boolean))
      count++;
  });

  return count;
};
