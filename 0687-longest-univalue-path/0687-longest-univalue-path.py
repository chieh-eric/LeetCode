# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        max_path = [0]

        def dfs(node,parent):
            if not node:
                return 0

            left = dfs(node.left,node)
            right = dfs(node.right,node)

            max_path[0] = max(max_path[0],left+right)

            if parent and node.val == parent.val:
                return max(left,right) + 1
            else:
                return 0

        

        dfs(root, None)
        return max_path[0]