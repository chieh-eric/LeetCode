import bisect
class Solution(object):
    def numberOfPairs(self, nums1, nums2, diff):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type diff: int
        :rtype: int
        """
        l = SortedList()
        res = 0
        for a, b in zip(nums1,nums2):
            idx = bisect.bisect_right(l,a-b)
            res += idx
            l.add(a-b-diff)
        return res