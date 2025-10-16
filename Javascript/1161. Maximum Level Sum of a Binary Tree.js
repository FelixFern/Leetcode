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
var maxLevelSum = function (root) {
  let max = root.val;
  let maxLevel = 1;

  const bfs = (root) => {
    const queue = [root];
    let currLevel = 0;

    while (queue.length > 0) {
      const depthSize = queue.length;
      let levelSum = 0;
      currLevel++;

      for (let i = 0; i < depthSize; i++) {
        const curr = queue.shift();
        levelSum += curr.val;
        if (curr.left) queue.push(curr.left);
        if (curr.right) queue.push(curr.right);
      }
      if (levelSum > max) {
        maxLevel = currLevel;
        max = levelSum;
      }
    }
  };

  bfs(root);
  return maxLevel;
};
