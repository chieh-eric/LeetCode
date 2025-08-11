from collections import defaultdict
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        n = len(nums)
        prefix = [0]*(n+1)
        cur = 0
        count = Counter()
        
        for i in range(1,n+1):
            cur += nums[i-1]
            prefix[i] = cur
        #print(prefix)

        total = 0
        for i in range(n+1):   
            total += count[prefix[i]-k]
            count[prefix[i]] += 1
        return total
