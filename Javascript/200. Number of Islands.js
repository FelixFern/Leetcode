/**
 * @param {character[][]} grid
 * @return {number}
 */
var numIslands = function (grid) {
  let res = 0;
  const width = grid.length;
  const height = grid[0].length;

  const safeIndex = (val, max) => Math.min(Math.max(val, 0), max);

  const traverse = (i, j) => {
    const step = [
      [0, 1],
      [1, 0],
      [-1, 0],
      [0, -1],
    ];

    step.forEach(([x, y]) => {
      const [newX, newY] = [
        safeIndex(i + x, width - 1),
        safeIndex(j + y, height - 1),
      ];
      if (grid[newX][newY] == "1") {
        grid[newX][newY] = "0";
        traverse(newX, newY);
      }
    });
  };

  for (let i = 0; i < width; i++) {
    for (let j = 0; j < height; j++) {
      if (grid[i][j] == "1") {
        grid[i][j] = "0";
        traverse(i, j);
        res += 1;
      }
    }
  }

  return res;
};
