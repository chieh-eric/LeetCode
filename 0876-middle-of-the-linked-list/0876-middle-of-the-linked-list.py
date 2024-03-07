# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = head
        leng = 0
        half = 0
        while count:
            count = count.next
            leng += 1
        half = leng//2
        for i in range(half):
            head = head.next
        return head