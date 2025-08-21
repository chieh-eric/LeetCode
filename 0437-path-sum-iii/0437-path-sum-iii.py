# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: int
        """
        states = Counter()
        states[0] = True
        def dfs(node,cur):
            if not node:
                return 0
            
            count = 0
            cur += node.val
            
            if cur - targetSum in states:
                count += states[cur-targetSum]
            states[cur] += 1
            count += dfs(node.left, cur)
            count += dfs(node.right, cur)
            states[cur] -= 1
            if states[cur] == 0:
                del states[cur]
            
            return count
        return dfs(root,0)