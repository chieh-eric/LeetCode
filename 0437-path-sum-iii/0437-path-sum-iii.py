# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: int
        """
        def check(node, cur):
            if not node:
                return 0

            valid = 0
            cur = node.val + cur
            if cur == targetSum:
                valid  += 1
            
            valid += check(node.left,cur) + check(node.right, cur)
            return valid
        
        def dfs(node):
            if not node:
                return 0
            
            count = check(node,0) + dfs(node.left) + dfs(node.right)
            
            return count
        return dfs(root)