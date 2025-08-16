# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        prev_val = -101
        cur_node = head
        while cur_node:
            cur_val = cur_node.val
            prev_node = cur_node
            while cur_node and cur_val == cur_node.val:
                cur_node = cur_node.next
            prev_node.next = cur_node
            if not cur_node:
                break
            prev_val = cur_node.val
        return head
            