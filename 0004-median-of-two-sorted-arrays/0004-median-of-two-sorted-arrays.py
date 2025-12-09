class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        n = len(nums1)
        m = len(nums2)

        total = m + n
        half = (total + 1) // 2
        left = 0 
        right = n

        while left <= right:
            partition1 = (left + right) // 2
            partition2 = half - partition1

            max_left1 = -float('inf') if partition1 == 0 else nums1[partition1-1]
            min_right1 = float('inf') if partition1 == n else nums1[partition1]

            max_left2 = -float('inf') if partition2 == 0 else nums2[partition2 - 1]
            min_right2 = float('inf') if partition2 == m else nums2[partition2]

            if max_left1 <= min_right2 and max_left2 <= min_right1:
                if total % 2 == 1:
                    return max(max_left1, max_left2)
                else:
                    return (max(max_left2, max_left1) + min(min_right1, min_right2))/2.0
            elif max_left1 > min_right2:
                right = partition1 - 1
            else:
                left = partition1 + 1
        return 0
            