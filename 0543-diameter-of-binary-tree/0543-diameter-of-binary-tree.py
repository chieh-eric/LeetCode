# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        max_path = [0]
        def dfs(node):
            if not node:
                return 0
            
            left = dfs(node.left) 
            right = dfs(node.right) 

            max_path[0] = max(max_path[0],left+right)

            return max(left,right) + 1

        dfs(root)
        return max_path[0]