from collections import defaultdict
class Solution(object):
    def longestEqualSubarray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        dic = defaultdict(list)
        for i in range(n):
            dic[nums[i]].append(i)
        
        max_len = 1
        for key in dic:
            arr = dic[key]
            left = 0
            for right in range(len(arr)):
                #print(left)
                while left < right and arr[right] - arr[left] - (right-left) > k:
                    left += 1
                max_len = max(max_len, right - left + 1)
        return max_len

        