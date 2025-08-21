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
        odd = head
        if not head:
            return None
        start_even = even = head.next

        while not even:
            return head
        
        while (odd and odd.next) or (even and even.next):
            if odd.next:
                if not odd.next.next:
                    odd.next = None
                else:
                    odd.next = odd.next.next
                    odd = odd.next

            if even.next:
                if not even.next.next:
                    even.next = None
                else:
                    even.next = even.next.next
                even = even.next

        #print(head)
        #print(start_even)
        odd.next = start_even
        return head
        

        

        