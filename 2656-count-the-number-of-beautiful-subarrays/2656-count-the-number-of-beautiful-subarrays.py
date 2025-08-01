class Solution(object):
    def beautifulSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        n = len(nums)
        prefix = [0]*n
        prefix[0] = nums[0]
        for i in range(1,n):
            prefix[i] = prefix[i-1]^nums[i]
        
        dic = {}
        count = 0
        for i in range(n):
            if prefix[i] == 0:
                count += 1
            
            if prefix[i] not in dic:
                dic[prefix[i]] = 1
            else:
                count += dic[prefix[i]]
                dic[prefix[i]] += 1
        return count
                