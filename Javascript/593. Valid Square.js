/**
 * @param {number[]} p1
 * @param {number[]} p2
 * @param {number[]} p3
 * @param {number[]} p4
 * @return {boolean}
 */

const distance = ([a1, a2], [b1, b2]) => pythagoras(a1 - b1, a2 - b2);

var validSquare = function (p1, p2, p3, p4) {
  const set = new Set();

  a = distance(p1, p2);
  b = distance(p1, p3);
  c = distance(p1, p4);
  d = distance(p2, p3);
  e = distance(p2, p4);
  f = distance(p3, p4);

  set.add(a);
  set.add(b);
  set.add(c);
  set.add(d);
  set.add(e);
  set.add(f);

  return set.size == 2 && !set.has(0);
};
