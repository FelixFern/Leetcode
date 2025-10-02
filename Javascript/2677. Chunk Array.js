/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array}
 */
var chunk = function (arr, size) {
  const res = [];
  let temp = [];

  arr.forEach((val, i) => {
    temp.push(val);
    if ((i + 1) % size === 0) {
      res.push([...temp]);
      temp = [];
    }
  });

  if (temp.length > 0) res.push(temp);

  return res;
};
