# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()
        dummy.next = None
        cur = head
        while cur:
            nxt_pointer = dummy.next
            dummy.next = cur
            next_one = cur.next
            cur.next = nxt_pointer
            cur = next_one
        return dummy.next
