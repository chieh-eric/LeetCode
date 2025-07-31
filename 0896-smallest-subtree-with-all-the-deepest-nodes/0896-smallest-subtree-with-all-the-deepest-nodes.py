# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def subtreeWithAllDeepest(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        def dfs(node,distance):
            if not node:
                return None, distance
            
            left, dl = dfs(node.left,distance+1)
            right, dr = dfs(node.right,distance+1)

            if dl > dr:
                return left, dl
            elif dr > dl:
                return right, dr
            else:
                return node, dl

        return dfs(root,0)[0]