# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        node_1 = list1
        node_2 = list2
        node_3 = ListNode()
        head_3 = node_3
        while node_1 and node_2:
            if node_1.val >= node_2.val:
                node_3.next = node_2
                node_3 = node_2
                next_node = node_2.next
                node_2 = next_node
            else:
                node_3.next = node_1
                node_3 = node_1
                next_node = node_1.next
                node_1 = next_node
                
        while node_1!=None:
            node_3.next = node_1
            node_3 = node_1
            next_node = node_1.next
            node_1 = next_node
        while node_2!=None:
            node_3.next = node_2
            node_3 = node_2
            next_node = node_2.next
            node_2 = next_node
                
        return head_3.next