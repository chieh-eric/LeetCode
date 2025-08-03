# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countPairs(self, root, distance):
        """
        :type root: Optional[TreeNode]
        :type distance: int
        :rtype: int
        """
        self.count = 0

        def dfs(node):
            if not node:
                return []
            
            if not node.left and not node.right:
                return [1]
            
            left = dfs(node.left)
            right = dfs(node.right)

            for l in left:
                for r in right:
                    if l + r <= distance:
                        self.count += 1
            return [val + 1 for val in left+right]
        dfs(root)
        return self.count
            
