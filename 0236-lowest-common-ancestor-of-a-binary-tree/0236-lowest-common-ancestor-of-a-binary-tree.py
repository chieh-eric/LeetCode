# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        def dfs(node):
            if not node:
                return None
            left = dfs(node.left)
            right = dfs(node.right)
       

            if node == p or node  == q:
                return node
            
            if left and right:
                return node
            
            if left:
                return left
            
            if right:
                return right

            return None
        return dfs(root)

        