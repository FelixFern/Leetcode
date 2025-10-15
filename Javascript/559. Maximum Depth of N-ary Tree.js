/**
 * // Definition for a _Node.
 * function _Node(val,children) {
 *    this.val = val === undefined ? null : val;
 *    this.children = children === undefined ? null : children;
 * };
 */

/**
 * @param {_Node|null} root
 * @return {number}
 */
var maxDepth = function (root) {
  if (root === null) return 0;

  const dfs = (root, depth) => {
    let depths = [];
    if (root?.children.length === 0) return depth;

    root.children.forEach((child) => {
      depths.push(dfs(child, depth + 1));
    });
    return Math.max(...depths);
  };

  return dfs(root, 1);
};
