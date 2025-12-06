# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head:
            return None
        
        odd, even = head, head.next
        cur_even = even

        while cur_even and cur_even.next:
            odd.next = cur_even.next
            odd = odd.next
            cur_even.next = cur_even.next.next
            cur_even = cur_even.next
        
        odd.next = even
        return head