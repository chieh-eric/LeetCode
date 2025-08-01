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
        res = [0]

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
                        res[0] += 1
            
            return [x + 1 for x in left + right if x + 1 <= distance]


        dfs(root)
        return res[0]

