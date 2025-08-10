# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def allPossibleFBT(self, n):
        """
        :type n: int
        :rtype: List[Optional[TreeNode]]
        """
        dp = {}
        res = []
        if (n+1) % 2:
            return []

        def dfs(v):
            if v == 1:
                return [TreeNode()]
            
            res = []
            for i in range(1,v, 2):
                right = v - i - 1
                for left_sub in dfs(i):
                    for right_sub in dfs(right):
                        root = TreeNode()
                        root.left = left_sub
                        root.right = right_sub
                        res.append(root)
            return res

       
        return dfs(n)
                
