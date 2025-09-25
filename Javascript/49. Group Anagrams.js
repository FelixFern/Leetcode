/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function (strs) {
  const sortedStrs = strs.map((v) =>
    v
      .split("")
      .map((a) => a)
      .sort()
      .join("")
  );
  const res = {};

  strs.forEach((val, idx) => {
    const key = sortedStrs[idx];
    if (!res[key]) res[key] = [val];
    else res[key].push(val);
  });

  return Object.values(res);
};
