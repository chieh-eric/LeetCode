# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = head
        fast = head
        meet = None
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                meet = fast
                break
        if not meet:
            return None
        
        cur = head
        while cur != meet:
            cur = cur.next
            meet = meet.next
        return cur 
