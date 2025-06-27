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
      
        def dfs(val):
            if val in dp:
                return dp[val]

            if not (val % 2):
                return []
            
            if val == 1:
                return [TreeNode(0)]

            res = []
            for left in range(1,val,2):
                right = val - left - 1
                for left_sub in dfs(left):
                    for right_sub in dfs(right):
                        root = TreeNode(0)
                        root.left = left_sub
                        root.right = right_sub
                        res.append(root)
            dp[val] = res
            return res
        return dfs(n)
