/**
 * @param {string} s
 * @return {string}
 */
var sortVowels = function (s) {
  const order = {
    A: 0,
    E: 1,
    I: 2,
    O: 3,
    U: 4,
    a: 5,
    e: 6,
    i: 7,
    o: 8,
    u: 9,
  };
  const vowels = Object.keys(order);
  const idxs = [];

  let res = s.split("");
  let p = 0;
  let count = Array(10).fill(0);

  s.split("").forEach((val, idx) => {
    if (order[val] !== undefined) {
      count[order[val]]++;
      idxs.push(idx);
    }
  });

  for (let i = 0; i < count.length; i++) {
    while (count[i] > 0) {
      res[idxs[p]] = vowels[i];
      p++;
      count[i]--;
    }
  }
  return res.join("");
};
