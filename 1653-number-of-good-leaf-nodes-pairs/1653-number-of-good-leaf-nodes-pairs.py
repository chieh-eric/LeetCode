from collections import defaultdict
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
        graph = defaultdict(list)
        leaf = set()

        def buildGraph(node,parent):
            if not node:
                return
            
            if parent:
                graph[parent].append(node)
                graph[node].append(parent)

            if node.left is None and node.right is None:
                leaf.add(node)
            
            buildGraph(node.left,node)
            buildGraph(node.right,node)
        buildGraph(root,None)

        def dfs(node,from_node,depth):
            if not node or depth > distance:            
                return 0

            if node in visited:
                return 0

            count = 0
            visited.add(node)
            if node in leaf and node != start:
                count += 1

            for child in graph[node]:
                if child != from_node:
                    count += dfs(child,node,depth+1)

            return count
        
        res = 0
        for start in leaf:
            visited = set()
            res += dfs(start,None,0)
        return res / 2
