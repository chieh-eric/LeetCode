# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inlist = {}
        for i in range(len(inorder)):
            inlist[inorder[i]] = i
        def array_to_list(left,right):
            nonlocal postorder_index
            if left > right:
                return None
            root_val = postorder[postorder_index]
            root_index = inlist[root_val]
            root = TreeNode(root_val)
            postorder_index -=1
            
            root.right = array_to_list(root_index+1,right)
            root.left = array_to_list(left,root_index-1)
            
            return root
            
        postorder_index = len(postorder) - 1
        return array_to_list(0,len(postorder)-1)