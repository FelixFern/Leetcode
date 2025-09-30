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
 * @return {TreeNode}
 */
var invertTree = function(root) {
    const dfs = (root) => {
        if(root?.val === undefined) return 
        
        const temp = root.left
        
        root.left = root.right
        root.right = temp

        dfs(root.left)
        dfs(root.right)
    }

    dfs(root)

    return root
};