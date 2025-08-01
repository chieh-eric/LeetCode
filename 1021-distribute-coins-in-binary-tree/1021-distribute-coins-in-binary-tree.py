# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def distributeCoins(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        move = [0]
        def dfs(node):
            if not node:
                return 0
           
            
            left = dfs(node.left)
            right = dfs(node.right)
           
            move[0] += abs(node.val + left + right - 1)
            return node.val + left + right - 1
        dfs(root)
        return move[0]