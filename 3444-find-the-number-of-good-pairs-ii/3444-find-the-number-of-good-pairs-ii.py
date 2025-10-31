from collections import defaultdict
class Solution(object):
    def numberOfPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: int
        """
        # Appraoch: make a new list of nums2
        # Find the maximum value of nums1
        # Use dictionary of new nums2 -> key will be the multiply value for this element, value -> # of this element
        # nums2 = [1,3,4] , max_val = 4
        # dic[1] = 1, dic[2] = 1, dic[3] = 2, dic[4] = 2

        new_nums2 = defaultdict(int)
        for num in nums2:
            new_nums2[num*k] += 1

        dic = defaultdict(int)
        max_val = max(nums1)
        for key in new_nums2:
            start = key
            while start <= max_val:
                dic[start] += new_nums2[key]
                start += key

        nums1_dic = defaultdict(int)
        for num in nums1:
            nums1_dic[num] += 1

        pairs = 0
        for key in nums1_dic:
            pairs += nums1_dic[key]*dic[key]
        return pairs
