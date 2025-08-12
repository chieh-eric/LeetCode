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
        res = []
        memo = {}
        def dfs(val):
            if val in memo:
                return memo[val]

            if val % 2 == 0:
                return []
            
            if val == 1:
                return [TreeNode()]      
            
            cur = []

            for i in range(1,val,2):
                right_val = val - i - 1
                for l in dfs(i):
                    for r in dfs(right_val):
                        root = TreeNode()
                        root.left = l
                        root.right = r
                        cur.append(root)
            memo[val] = cur
            return cur
        return dfs(n)