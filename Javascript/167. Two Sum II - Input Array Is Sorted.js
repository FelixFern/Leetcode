/**
 * @param {number[]} numbers
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (numbers, target) {
  let left = 0;
  let right = numbers.length - 1;

  while (left < right) {
    const [a, b] = [numbers[left], numbers[right]];

    if (a + b === target) break;
    if (a + b < target) left++;
    else right--;
  }

  return [left + 1, right + 1];
};
