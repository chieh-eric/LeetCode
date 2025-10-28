class Solution(object):
    def countValidSelections(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        prefix = [0]*(n+1)
        suffix = [0]*(n+1)

        for i, num in enumerate(nums,1):
            prefix[i] = prefix[i-1] + num
        
        for i in range(n-2, -1, -1):
            suffix[i] = suffix[i+1] + nums[i+1]
        
        #print(prefix)
        #print(suffix)
        
        count = 0
        for i in range(n):
            if nums[i] == 0:
                if prefix[i] == suffix[i]:
                    count += 2
                elif abs(prefix[i] - suffix[i]) == 1:
                    count += 1
            
        return count