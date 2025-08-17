# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        count = 1
        cur = head
        if not cur:
            return None
        while cur.next:
            count += 1
            cur = cur.next
        cur.next = head

            
        r = k % count
        cur = prev = head
        
        for _ in range(count-r):
            prev = cur
            cur = cur.next
        prev.next = None
        return cur