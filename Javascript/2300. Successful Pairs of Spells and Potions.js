/**
 * @param {number[]} spells
 * @param {number[]} potions
 * @param {number} success
 * @return {number[]}
 */
var successfulPairs = function (spells, potions, success) {
  const res = [];
  potions.sort((a, b) => a - b);

  for (let i = 0; i < spells.length; i++) {
    let lp = 0;
    let rp = potions.length - 1;
    let valid = potions.length;

    while (lp <= rp) {
      const mid = Math.floor((lp + rp) / 2);
      const curr = spells[i] * potions[mid];
      if (curr >= success) {
        rp = mid - 1;
        valid = mid;
      } else {
        lp = mid + 1;
      }
    }
    res.push(potions.length - valid);
  }
  return res;
};
