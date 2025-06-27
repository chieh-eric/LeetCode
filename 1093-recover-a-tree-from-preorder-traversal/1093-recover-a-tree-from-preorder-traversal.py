import re
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
        nodes = re.findall(r'(-*)(\d+)',traversal)
        parsed = [(len(dash),int(val)) for dash,val in nodes]
        print(parsed)
        
        stack = []
        for depth, val in parsed:
            node = TreeNode(val)

            while depth < len(stack):
                stack.pop()
            
            if stack:
                parent = stack[-1]
                if not parent.left:
                    parent.left = node
                else:
                    parent.right = node
            stack.append(node) 
        return stack[0]