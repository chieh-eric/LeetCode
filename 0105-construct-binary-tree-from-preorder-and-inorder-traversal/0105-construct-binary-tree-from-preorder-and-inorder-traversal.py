# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        in_map ={}
        for i in range(len(inorder)):
            in_map[inorder[i]] = i
        def array_to_tree(left,right):
            nonlocal preorder_index
            if (left > right):
                return None
            root_value = preorder[preorder_index]
            root_index = in_map[root_value]
            root = TreeNode(root_value)
            preorder_index += 1
            
            root.left = array_to_tree(left,root_index-1)
            root.right = array_to_tree(root_index+1,right)
            
            return root
        preorder_index = 0
        return array_to_tree(0,len(inorder)-1)