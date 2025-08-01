from collections import defaultdict
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def createBinaryTree(self, descriptions):
        """
        :type descriptions: List[List[int]]
        :rtype: Optional[TreeNode]
        """
        children = set()
        nodes = set()
        graph = defaultdict(list)

        for parent, child, isLeft in descriptions:
            nodes.add(parent)
            children.add(child)
            graph[parent].append((child,isLeft))

        root = (nodes-children).pop()

        def build(val):
            node = TreeNode(val)

            for child, isLeft in graph[val]:
                if isLeft:
                    node.left = build(child)
                else:
                    node.right = build(child)
            return node
        return build(root)