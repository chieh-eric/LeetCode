from collections import defaultdict
class Solution(object):
    def maximumSetSize(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        length = len(nums1) // 2
        n1 = set(nums1)
        n2 = set(nums2)
        inter_num = len(n1&n2)

        diff = 0
        diff += len(n1) - length if len(n1) >= length else 0
        diff += len(n2) - length if len(n2) >= length else 0  

        return len(n1) + len(n2) - max(diff,inter_num)   
