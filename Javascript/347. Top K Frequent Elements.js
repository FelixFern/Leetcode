/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function (nums, k) {
  const count = {};
  const largest = [];
  for (num of nums) {
    count[num] = (count[num] ?? 0) + 1;
  }

  const maxCount = Math.max(...Object.values(count));
  let sort = new Array(maxCount + 1).fill(null);

  Object.entries(count).forEach(([num, total]) => {
    if (!sort[total]) {
      sort[total] = [num];
    } else {
      sort[total].push(num);
    }
  });

  let res = [];
  let p = maxCount;
  while (k > res.length && p >= 0) {
    while ((sort[p] ?? []).length > 0) {
      const temp = sort[p].pop();
      res.push(parseInt(temp));
    }
    p--;
  }

  return res;
};
