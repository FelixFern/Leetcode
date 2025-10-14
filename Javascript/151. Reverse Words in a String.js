/**
 * @param {string} s
 * @return {string}
 */
var reverseWords = function (s) {
  let splitted = s.split(" ").filter(Boolean);
  return splitted.reverse().join(" ");
};
