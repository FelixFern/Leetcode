/**
 * @param {number[][]} points
 * @return {number}
 */
var largestTriangleArea = function (points) {
  const calculateTriangle = (...points) => {
    const a = points[0];
    const b = points[1];
    const c = points[2];

    return (
      0.5 *
      Math.abs(
        a[0] * (b[1] - c[1]) + b[0] * (c[1] - a[1]) + c[0] * (a[1] - b[1])
      )
    );
  };

  let res = 0;

  for (let i = 0; i < points.length - 2; i++) {
    for (let j = i + 1; j < points.length - 1; j++) {
      for (let k = j + 1; k < points.length; k++) {
        const area = calculateTriangle(points[i], points[j], points[k]);
        if (area > res) res = area;
      }
    }
  }

  return res;
};
