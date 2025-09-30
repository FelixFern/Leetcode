/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
var goodNodes = function (root) {
  let res = 0;

  const dfs = (root, max = -Infinity) => {
    if (root?.val === undefined) return;

    if (root.val >= max) {
      res += 1;
    }

    dfs(root.left, Math.max(root.val, max));
    dfs(root.right, Math.max(root.val, max));
  };

  dfs(root);

  return res;
};
