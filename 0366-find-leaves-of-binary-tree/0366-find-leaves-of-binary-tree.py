# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findLeaves(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        mark = {}
        def dfs(node):
            if not node:
                return 
            
            if not node.left and not node.right:
                mark[node] = 0
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            mark[node] = max(left,right) + 1
            return mark[node]
        dfs(root)
        #print(mark)
        n = max(mark.values()) + 1
        #print(n)
        res = [[] for _ in range(n)]
        
        for key in mark:
            res[mark[key]].append(key.val)
        return res