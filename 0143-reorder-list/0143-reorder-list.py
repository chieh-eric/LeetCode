# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        count = 0
        head_cur = head
        while head_cur != None:
            count+=1
            head_cur = head_cur.next
        if count==1:
            head = head
        else: 
            half = count//2
            tail_cur = head

            for i in range(half):
                tail_cur = tail_cur.next
            # Reverse
            prev = None
            cur = tail_cur
            while cur != None:      
                nextNode = cur.next
                cur.next = prev
                prev = cur
                cur = nextNode
            tp = head
            for i in range(half-1):
                tp = tp.next
            tp.next = None
            head_t = head
            while head_t and prev:
                headNext = head_t.next
                head_t.next = prev
                head_t = headNext
                prevNext = prev.next
                if head_t == None:
                    break
                prev.next = head_t
                prev = prevNext

        

        
        