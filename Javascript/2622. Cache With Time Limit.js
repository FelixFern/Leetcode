var TimeLimitedCache = function () {
  this.cache = {};
  this.cacheTimeout = {};
};

/**
 * @param {number} key
 * @param {number} value
 * @param {number} duration time until expiration in ms
 * @return {boolean} if un-expired key already existed
 */
TimeLimitedCache.prototype.set = function (key, value, duration) {
  let existed = false;
  if (this.cache[key]) {
    clearTimeout(this.cacheTimeout[key]);
    existed = true;
  }

  this.cache[key] = [value, duration];
  this.cacheTimeout[key] = setTimeout(() => {
    delete this.cache[key];
  }, duration);

  return existed;
};

/**
 * @param {number} key
 * @return {number} value associated with key
 */
TimeLimitedCache.prototype.get = function (key) {
  return this.cache?.[key]?.[0] ?? -1;
};

/**
 * @return {number} count of non-expired keys
 */
TimeLimitedCache.prototype.count = function () {
  return Object.entries(this.cache).length;
};

/**
 * const timeLimitedCache = new TimeLimitedCache()
 * timeLimitedCache.set(1, 42, 1000); // false
 * timeLimitedCache.get(1) // 42
 * timeLimitedCache.count() // 1
 */
