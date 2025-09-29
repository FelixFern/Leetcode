/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {boolean}
 */
var isSameTree = function (p, q) {
  const dfs = (a, b) => {
    if (a?.val === undefined && b?.val === undefined) return true;
    if (a?.val !== b?.val) {
      return false;
    } else if (a.val === b.val) {
      return dfs(a.left, b.left) && dfs(a.right, b.right);
    }
  };

  return dfs(p, q);
};
