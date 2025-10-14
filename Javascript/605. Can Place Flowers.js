/**
 * @param {number[]} flowerbed
 * @param {number} n
 * @return {boolean}
 */
var canPlaceFlowers = function (flowerbed, n) {
  if (n === 1 && flowerbed.length === 1 && flowerbed[0] === 0) return true;

  let emptyValid = 0;

  for (let i = 0; i < flowerbed.length; i++) {
    if (i === 0) {
      if (flowerbed[i] === 0 && flowerbed[i + 1] === 0) {
        emptyValid += 1;
        flowerbed[i] = 1;
      }
    } else if (i === flowerbed.length - 1) {
      if (flowerbed[i] === 0 && flowerbed[i - 1] === 0) {
        emptyValid += 1;
      }
    } else {
      if (
        flowerbed[i - 1] === 0 &&
        flowerbed[i + 1] === 0 &&
        flowerbed[i] === 0
      ) {
        emptyValid += 1;
        flowerbed[i] = 1;
      }
    }
  }
  return emptyValid >= n;
};
