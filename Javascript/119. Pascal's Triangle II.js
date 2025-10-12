/**
 * @param {number} rowIndex
 * @return {number[]}
 */
var getRow = function (rowIndex) {
  const generatePascal = (curr, row) => {
    let temp = new Array(row + 1).fill(0);

    temp[0] = 1;
    temp[row] = 1;
    temp = temp.map((val, idx) => {
      if (idx === 0 || idx === row) return val;
      return curr[idx] + curr[idx - 1];
    });

    if (row < rowIndex) {
      return generatePascal(temp, row + 1);
    }
    return temp;
  };
  return generatePascal([], 0);
};
