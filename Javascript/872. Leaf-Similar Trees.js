/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root1
 * @param {TreeNode} root2
 * @return {boolean}
 */
var leafSimilar = function (root1, root2) {
  let root1Leaf = [];
  let root2Leaf = [];

  const dfs = (root, arr) => {
    if (!root.left && !root.right) {
      arr.push(root.val);
    }
    if (root?.left) dfs(root.left, arr);
    if (root?.right) dfs(root.right, arr);
  };

  dfs(root1, root1Leaf);
  dfs(root2, root2Leaf);

  return JSON.stringify(root1Leaf) === JSON.stringify(root2Leaf);
};
