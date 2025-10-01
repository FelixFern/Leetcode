/**
 * @param {number} numBottles
 * @param {number} numExchange
 * @return {number}
 */
var numWaterBottles = function (numBottles, numExchange) {
  let total = 0;

  const drink = (bottle, empty) => {
    if (empty < numExchange && bottle === 0) return;
    total += bottle;
    const emp = bottle + empty;
    const curr = Math.floor(emp / numExchange);
    drink(curr, emp - curr * numExchange);
  };

  drink(numBottles, 0);
  return total;
};
