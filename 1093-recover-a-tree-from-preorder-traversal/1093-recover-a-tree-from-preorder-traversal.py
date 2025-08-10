# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recoverFromPreorder(self, traversal):
        """
        :type traversal: str
        :rtype: Optional[TreeNode]
        """
        dic = {}

        depth = 0
        i = 0
        n = len(traversal)

        while i < n:
            depth = 0

            if traversal[i] == "-":
                while traversal[i] == "-":
                    depth += 1
                    i += 1
            start = i
            while i < n and traversal[i] != "-":
                i += 1
            val = int(traversal[start:i])
            
            node = TreeNode(val)
            if depth in dic:
                if dic[depth].left:
                    dic[depth].right = node
                else:
                    dic[depth].left = node
            dic[depth+1] = node

        return dic[1]
        


