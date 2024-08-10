/**
 * @param {Function[]} functions
 * @return {Function}
 */
var compose = function(functions) {
    const val = (x) => functions.reverse().reduce((p, c) => {
        return c(p)
    }, x)
    return function(x) {
        return val(x)
    }
};

/**
 * const fn = compose([x => x + 1, x => 2 * x])
 * fn(4) // 9
 */