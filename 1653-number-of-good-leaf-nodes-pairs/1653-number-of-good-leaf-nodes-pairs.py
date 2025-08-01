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
 
        def build(node, parent):
            if not node:
                return 

            if parent:
                graph[parent].append(node)
                graph[node].append(parent)
            
            if not node.left and not node.right:
                leaf.add(node)
            
            build(node.left,node)
            build(node.right,node)
            
        build(root,None)

        def dfs(node,parent,step):
            if not node or step > distance or node in visited:
                return 0
            visited.add(node)
            if node in leaf and node != i:
                return 1

            valid = 0
           
           
            for nei in graph[node]:
                if nei == parent:
                    continue

                if step + 1 <= distance:
                    valid += dfs(nei,node,step+1)   
            
            return valid

        res = 0
        for i in leaf:
            visited = set()
            res += dfs(i,None,0)
        return res / 2
