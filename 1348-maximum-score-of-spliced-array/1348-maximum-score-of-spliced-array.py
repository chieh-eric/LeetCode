class Solution(object):
    def maximumsSplicedArray(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        n = len(nums1)
        diff = [nums1[i]-nums2[i] for i in range(n)]
        #print(diff)
        min_val = max_val = cur_min = cur_max = 0
        for i in range(n):
            cur_min = min(diff[i],cur_min+diff[i])
            cur_max = max(diff[i],cur_max+diff[i])

            min_val = min(min_val, cur_min)
            max_val = max(max_val, cur_max)
        #print(min_val)
        #print(max_val)
        return max(sum(nums1)-min_val, sum(nums2)+max_val)
