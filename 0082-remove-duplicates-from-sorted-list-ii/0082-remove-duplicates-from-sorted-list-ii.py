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
        dummy = ListNode(0,head)
        prev = dummy
        cur = head
        if not head or not head.next:
            return head
            
        while cur:

            is_duplicate = False

            while cur and cur.next and cur.next.val == cur.val:
                cur = cur.next
                is_duplicate = True
            
            if is_duplicate:
                prev.next = cur.next
            else:
                prev = prev.next
            cur = cur.next

        return dummy.next

            

        
        
                

