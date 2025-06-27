# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sufficientSubset(self, root, limit):
        """
        :type root: Optional[TreeNode]
        :type limit: int
        :rtype: Optional[TreeNode]
        """
        nodes = {}
        valid = set()
        def dfs(node,path):
            if node is None:
                return
            path.append(node)
            if not node.right and not node.left:
                total = sum(node.val for node in path)
                if total >= limit:
                    for node in path:
                        valid.add(node)
            dfs(node.left,path)
            dfs(node.right,path)
            path.pop()

        dfs(root,[])

        def remove(node):
            if node is None:
                return None
            if node not in valid:
                return None
            
            node.left = remove(node.left)
            node.right = remove(node.right)

            return node
        return remove(root)