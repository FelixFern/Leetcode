/**
 * @param {number} numBottles
 * @param {number} numExchange
 * @return {number}
 */
var maxBottlesDrunk = function (numBottles, numExchange) {
  let currNumExchange = numExchange;
  let totalBottle = 0;

  const drink = (full, empty) => {
    if (full === 0 && empty < currNumExchange) return;

    totalBottle += full;
    let totalEmpty = empty + full;
    let currFull = 0;
    while (totalEmpty >= currNumExchange) {
      totalEmpty -= currNumExchange;
      currNumExchange += 1;
      currFull += 1;
    }
    drink(currFull, totalEmpty);
  };
  drink(numBottles, 0);

  return totalBottle;
};
