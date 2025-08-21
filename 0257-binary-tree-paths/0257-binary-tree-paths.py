# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[str]
        """
        self.res = []
        def dfs(node, path):
            if not node:
                return 
            path = path + [str(node.val)]
            if not node.left and not node.right:
                #print(path)
                self.res.append("->".join(path))
                return
            
            dfs(node.left,path)
            dfs(node.right,path)
        dfs(root,[])
        return self.res