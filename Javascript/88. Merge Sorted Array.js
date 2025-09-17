/**
 * @param {number[]} nums1
 * @param {number} m
 * @param {number[]} nums2
 * @param {number} n
 * @return {void} Do not return anything, modify nums1 in-place instead.
 */
var merge = function (nums1, m, nums2, n) {
  a = m - 1;
  b = n - 1;
  c = m + n - 1;

  while (b >= 0) {
    if (nums1[a] > nums2[b]) {
      nums1[c] = nums1[a];
      c--;
      a--;
    } else {
      nums1[c] = nums2[b];
      c--;
      b--;
    }
  }
};
