/**
 * @param {string[]} words
 * @return {string[]}
 */
var removeAnagrams = function (words) {
  let counted = [];

  for (word of words) {
    let temp = Array(26).fill(0);
    for (s of word) {
      const idx = s.charCodeAt(0) - "a".charCodeAt(0);
      temp[idx] += 1;
    }
    counted.push([word, temp.join("")]);
  }

  let pointer = 1;
  console.log(counted);
  while (pointer < counted.length) {
    while (counted?.[pointer]?.[1] === counted?.[pointer - 1]?.[1]) {
      counted = counted.filter((_, idx) => idx != pointer);
    }
    pointer++;
  }
  return counted.map(([val]) => val);
};
