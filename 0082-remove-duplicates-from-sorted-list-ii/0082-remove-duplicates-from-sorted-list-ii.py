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
        cur = head
        dic = {}
        count = Counter()
        arr = []
        while cur:
            count[cur.val] += 1
            arr.append(cur.val)
            cur = cur.next

        start = ListNode()
        cur = start
        for node in arr:
            if count[node] == 1:
                cur.next = ListNode(node)
                cur = cur.next
        return start.next
        
        
                

