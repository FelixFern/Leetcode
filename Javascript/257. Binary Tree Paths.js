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
 * @return {string[]}
 */
var binaryTreePaths = function (root) {
  const res = [];

  const dfs = (root, path) => {
    console.log(path, root?.left, root?.right, root?.val);
    if (root?.val === undefined) return;
    if (root?.left === null && root?.right === null) {
      res.push([...path, root?.val].join("->"));
      return;
    }

    dfs(root?.left, [...path, root?.val]);
    dfs(root?.right, [...path, root?.val]);
  };

  dfs(root, []);
  return res;
};
