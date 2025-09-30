/**
 * @param {Function} fn
 * @return {Function}
 */
function memoize(fn) {
  const memo = new Map();
  return function (...args) {
    const key = args.join(",");
    if (memo.get(key) !== undefined) return memo.get(key);
    else {
      const res = fn(...args);
      memo.set(key, res);
      return res;
    }
  };
}

/**
 * let callCount = 0;
 * const memoizedFn = memoize(function (a, b) {
 *	 callCount += 1;
 *   return a + b;
 * })
 * memoizedFn(2, 3) // 5
 * memoizedFn(2, 3) // 5
 * console.log(callCount) // 1
 */
