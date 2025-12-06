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
            return head
        odd_start = head
        even_start = head.next

        prev_odd = None
        cur_odd = odd_start
        cur_even = even_start
        while (cur_odd and cur_odd.next) or (cur_even and cur_even.next):
            if cur_odd and cur_odd.next:
                cur_odd.next = cur_odd.next.next
                prev_odd = cur_odd
                cur_odd = cur_odd.next
            
            if cur_even and cur_even.next:
                cur_even.next = cur_even.next.next
                cur_even = cur_even.next
        
        if cur_odd:
            cur_odd.next = even_start
        else:
            prev_odd.next = even_start
        return head