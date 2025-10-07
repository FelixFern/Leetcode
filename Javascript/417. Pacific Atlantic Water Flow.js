/**
 * @param {number[][]} heights
 * @return {number[][]}
 */
var pacificAtlantic = function (heights) {
  const pacificOceans = new Set();
  const atlanticOceans = new Set();
  const pacificVisited = new Set();
  const atlanticVisited = new Set();

  const res = [];

  const safeCoord = (i, j) => {
    if (
      i >= 0 &&
      i <= heights.length - 1 &&
      j >= 0 &&
      j <= heights[0].length - 1
    )
      return [i, j];
    return [null, null];
  };

  const dfs = (i, j, ocean) => {
    const key = [i, j].join(",");
    if (ocean === "pac") {
      if (pacificOceans.has(key)) return;
      pacificOceans.add(key);
    }
    if (ocean === "atl") {
      if (atlanticOceans.has(key)) return;
      atlanticOceans.add(key);
    }

    const steps = [
      [0, 1],
      [1, 0],
      [0, -1],
      [-1, 0],
    ];

    for (step of steps) {
      const [x, y] = safeCoord(i + step[0], j + step[1]);

      if (x === null || y === null) continue;
      if (heights[i][j] <= heights[x][y]) dfs(x, y, ocean);
    }
  };

  const m = heights.length;
  const n = heights[0].length;

  for (let i = 0; i < m; i++) {
    dfs(i, 0, "pac");
    dfs(i, n - 1, "atl");
  }
  for (let j = 0; j < n; j++) {
    dfs(0, j, "pac");
    dfs(m - 1, j, "atl");
  }
  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      const key = [i, j].join(",");
      if (pacificOceans.has(key) && atlanticOceans.has(key)) res.push([i, j]);
    }
  }

  return res;
};
