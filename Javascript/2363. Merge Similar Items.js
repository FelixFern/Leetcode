/**
 * @param {number[][]} items1
 * @param {number[][]} items2
 * @return {number[][]}
 */
var mergeSimilarItems = function (items1, items2) {
  sums = {};

  items1.forEach(([id, val]) => {
    sums[id] = (sums[id] ?? 0) + val;
  });
  items2.forEach(([id, val]) => {
    sums[id] = (sums[id] ?? 0) + val;
  });

  return Object.entries(sums).map(([id, val]) => [Number(id), val]);
};
