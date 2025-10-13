/**
 * @param {number[][]} grid
 * @return {boolean}
 */
var checkValidGrid = function (grid) {
  let curr = 0;
  let currIdx = [-1, -1];
  const n = grid.length;
  const moves = [
    [2, 1],
    [2, -1],
    [-2, 1],
    [-2, -1],
    [1, 2],
    [1, -2],
    [-1, 2],
    [-1, -2],
  ];

  if (grid[0][0] !== 0) return false;

  const validMove = (val1, val2) => {
    if (val1 >= 0 && val1 <= n - 1 && val2 >= 0 && val2 <= n - 1) {
      return [val1, val2];
    }
    return [null, null];
  };

  for (let i = 0; i < n; i++) {
    if (currIdx[0] !== -1) break;
    for (let j = 0; j < n; j++) {
      if (grid[i][j] === 0) {
        currIdx = [i, j];
        break;
      }
    }
  }

  while (curr !== n * n - 1) {
    const [prevX, prevY] = currIdx;
    let valid = false;
    for (move of moves) {
      const [x, y] = validMove(prevX + move[0], prevY + move[1]);
      if (x === null) continue;
      if (grid[x][y] === curr + 1) {
        curr++;
        currIdx = [x, y];
        valid = true;
        break;
      }
    }
    if (!valid) break;
  }

  return curr === n * n - 1;
};
