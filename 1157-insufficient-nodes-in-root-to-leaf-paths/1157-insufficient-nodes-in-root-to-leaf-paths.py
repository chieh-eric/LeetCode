# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sufficientSubset(self, root, limit):
        """
        :type root: Optional[TreeNode]
        :type limit: int
        :rtype: Optional[TreeNode]
        """
        
        def dfs(node,pathSum):
            if not node:
                return None
            pathSum += node.val

            if not node.left and not node.right:
                return node if pathSum >= limit else None
            
            node.left = dfs(node.left,pathSum)
            node.right = dfs(node.right,pathSum)

            if not node.left and not node.right:
                return None
            
            return node
        return dfs(root,0)