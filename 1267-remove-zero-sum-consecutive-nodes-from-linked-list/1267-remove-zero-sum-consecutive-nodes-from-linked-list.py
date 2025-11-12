# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeZeroSumSublists(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Approach prefix sum, dic -> key(sum_val), val -> (node)
        # Store prefix sum in dic
        # Store 1, 3, 6, 3
        # 1, 3, 6, 3
        # 0, 1, 3, 0
        # 0, -2, -3, -2

        prefix = {}
        cur_val = 0
        dummy = ListNode()
        dummy.next = head
        cur_node = head
        prefix[0] = dummy

        while cur_node:
            cur_val += cur_node.val
            if cur_val in prefix:
                copy_dic = prefix.copy()
                delete_node = prefix[cur_val].next
                temp_val = cur_val
                while delete_node != cur_node:
                    temp_val += delete_node.val
                    del prefix[temp_val]
                    delete_node = delete_node.next
                prefix[cur_val].next = cur_node.next

            else:
                prefix[cur_val] = cur_node
            cur_node = cur_node.next
        return dummy.next
        