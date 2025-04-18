/**
 * @param {number[]} nums
 * @param {Function} fn
 * @param {number} init
 * @return {number}
 */
var reduce = function(nums, fn, init) {
  let res = init

  for(i of nums) {
      res = fn(res, i)
  }

  return res
};