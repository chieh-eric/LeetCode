class Solution(object):
    def minimumMountainRemovals(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        n = len(nums)
        incr = [1]*n
        decr = [1]*n

        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    incr[i] = max(incr[i],incr[j]+1)
        
        for i in range(n-1,-1,-1):
            for j in range(i+1,n):
                if nums[i] > nums[j]:
                    decr[i] = max(decr[i],decr[j]+1)
        
        length = 0
        for i in range(n):
            if incr[i] >=2 and decr[i] >=2:
                length = max(length,incr[i]+decr[i]-1)
        #print(incr)
        #print(decr)
        return n - length
