# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def btreeGameWinningMove(self, root, n, x):
        """
        :type root: Optional[TreeNode]
        :type n: int
        :type x: int
        :rtype: bool
        """
        # Use dfs to return the left and right subtree nodes number sum
        self.left = 0
        self.right = 0
        def dfs(node):
            if not node:
                return 0
            l = dfs(node.left)
            r = dfs(node.right)
            if node.val == x:
                self.left = l
                self.right = r
            return l + r + 1
        dfs(root)
        parent = n - self.left - self.right - 1
        return True if max(parent,self.left,self.right) > n//2 else False
            
        
        #    1
        #  2   3
        # 4  5