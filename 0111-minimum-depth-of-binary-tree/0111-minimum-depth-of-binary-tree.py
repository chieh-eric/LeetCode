# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        if root.left == None:
            return 1+self.minDepth(root.right)
        elif root.right == None:
            return 1+self.minDepth(root.left)
        else:
            leftHeight = self.minDepth(root.left)
            rightHeight = self.minDepth(root.right)
            return min(leftHeight,rightHeight)+1