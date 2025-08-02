# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getDirections(self, root, startValue, destValue):
        """
        :type root: Optional[TreeNode]
        :type startValue: int
        :type destValue: int
        :rtype: str
        """
        start_path = []
        dest_path = []
        def dfs(node,path,d):
            if not node:
                return 

            path.append((node.val,d))
            if node.val == startValue:
                start_path.extend(path[:])
            if node.val == destValue:
                dest_path.extend(path[:])

            left = dfs(node.left,path,0)
            right = dfs(node.right,path,1)
            path.pop()
        dfs(root,[],None)
        
       
        n = min(len(start_path),len(dest_path))
        index = 0
        for i in range(n):
            if start_path[i] == dest_path[i]:
                index = i
            else:
                break
    
        start_path = start_path[index+1:]
        dest_path = dest_path[index+1:]
        res = "U"*len(start_path)
        
        for _, d in dest_path:
            if d == 0:
                res += "L"
            else:
                res += "R"
        return res