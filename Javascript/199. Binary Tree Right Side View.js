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
 * @return {number[]}
 */
var rightSideView = function (root) {
  const bfs = (root) => {
    const queue = [root];
    const levels = [];

    while (queue.length > 0) {
      const depthSize = queue.length;
      const level = [];

      for (let i = 0; i < depthSize; i++) {
        const curr = queue.shift();
        level.push(curr?.val);
        if (curr?.left) queue.push(curr.left);
        if (curr?.right) queue.push(curr.right);
      }
      levels.push(level);
    }

    return levels.map((v) => v[v.length - 1]).filter((v) => v !== undefined);
  };

  return bfs(root);
};
