/**
 * @param {number[][]} nums1
 * @param {number[][]} nums2
 * @return {number[][]}
 */
var mergeArrays = function (nums1, nums2) {
  sums = {};

  nums1.forEach(([id, val]) => {
    sums[id] = (sums[id] ?? 0) + val;
  });
  nums2.forEach(([id, val]) => {
    sums[id] = (sums[id] ?? 0) + val;
  });

  return Object.entries(sums).map(([id, val]) => [Number(id), val]);
};
