# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited_node = set()
        cur_node = head
        while cur_node != None:
            if cur_node in visited_node:
                return True
            else:
                visited_node.add(cur_node)
            next_node = cur_node.next
            cur_node = next_node
        return False
            