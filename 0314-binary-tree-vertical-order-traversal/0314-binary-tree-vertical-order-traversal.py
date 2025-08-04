# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        group = []
        def dfs(node,pos,h):
            if not node:
                return
            group.append((pos,h,node.val))
            dfs(node.left,pos-1,h+1)
            dfs(node.right,pos+1,h+1)
        dfs(root,0,0)
        group.sort(key= lambda x:(x[0],x[1]))
        #print(group)
        res = []
        cur_pos = float('inf')
        i = 0
        n = len(group)
        while i < n:
            temp = []
            while i < n and cur_pos == group[i][0]:
                temp.append(group[i][2])
                i += 1

            if i < n:
                cur_pos = group[i][0]
            if temp:
                res.append(temp)
        return res