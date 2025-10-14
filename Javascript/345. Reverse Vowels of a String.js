/**
 * @param {string} s
 * @return {string}
 */
var reverseVowels = function (s) {
  const vowels = new Set(["a", "i", "u", "e", "o"]);
  let splitted = s.split("");
  const vowelIdx = [];
  const tempVowel = [];

  splitted.forEach((alp, idx) => {
    if (vowels.has(alp.toLowerCase())) {
      vowelIdx.push(idx);
      tempVowel.push(alp);
    }
  });

  vowelIdx.forEach((val, idx) => {
    splitted[val] = tempVowel[vowelIdx.length - idx - 1];
  });

  return splitted.join("");
};
