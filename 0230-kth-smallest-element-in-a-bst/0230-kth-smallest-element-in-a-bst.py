# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        inorder_list = []
        def inorder_travesal(root):
            if not root:
                return
            inorder_travesal(root.left)
            inorder_list.append(root.val)
            inorder_travesal(root.right)
        inorder_travesal(root)
        return inorder_list[k-1]

            