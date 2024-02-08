# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        ct_node = head
        cur = head
        prev = ListNode()
        while ct_node != None:
            count+=1
            ct_node = ct_node.next
        if count == n:
            return head.next
        for i in range(count-n):
            prev = cur
            cur = cur.next
        prev.next = cur.next
        return head