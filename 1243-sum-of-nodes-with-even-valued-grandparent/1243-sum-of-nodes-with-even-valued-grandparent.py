# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumEvenGrandparent(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def dfs(node,parent,grand):
            if not node:
                return 0
            count = 0
            if grand and grand.val % 2 == 0:
                count += node.val
            count += dfs(node.left,node,parent)
            count += dfs(node.right,node,parent)
            return count


        return dfs(root,None,None)
                            