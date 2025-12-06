# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        dic = {}
        cur = head
        while cur:
            if cur in dic:
                return True
            dic[cur] = True
            cur = cur.next
        return False
    