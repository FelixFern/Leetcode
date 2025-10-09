/**
 * @param {number[]} skill
 * @param {number[]} mana
 * @return {number}
 */
var minTime = function (skill, mana) {
  const [n, m] = [skill.length, mana.length];
  const times = new Array(n).fill(0);

  for (let j = 0; j < m; j++) {
    let currTime = 0;
    for (let i = 0; i < n; i++) {
      currTime = Math.max(currTime, times[i]) + skill[i] * mana[j];
    }
    times[n - 1] = currTime;

    for (let i = n - 2; i >= 0; i--) {
      times[i] = times[i + 1] - skill[i + 1] * mana[j];
    }
  }
  return times[n - 1];
};
