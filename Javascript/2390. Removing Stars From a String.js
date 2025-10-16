/**
 * @param {string} s
 * @return {string}
 */
var removeStars = function (s) {
  let splitted = s.split("");
  let res = [];

  for (alp of splitted) {
    if (alp === "*") {
      res.pop();
    } else {
      res.push(alp);
    }
  }

  return res.join("");
};
