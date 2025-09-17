/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function (s) {
  const stack = [];

  for (val of s) {
    const last = stack.length - 1;
    if (val === ")" && stack[last] === "(") {
      stack.pop();
    } else if (val === "}" && stack[last] === "{") {
      stack.pop();
    } else if (val === "]" && stack[last] === "[") {
      stack.pop();
    } else {
      stack.push(val);
    }
  }

  return stack.length === 0;
};
