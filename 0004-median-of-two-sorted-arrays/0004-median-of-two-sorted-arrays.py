class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        arr = sorted(nums1+nums2)
        n = len(nums1)
        m = len(nums2)
        mid = (n+m) // 2

        return arr[mid] if (n+m)%2 else (float(arr[mid]) + arr[mid-1])/2

