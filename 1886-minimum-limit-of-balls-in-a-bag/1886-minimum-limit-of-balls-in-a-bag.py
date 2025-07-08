class Solution(object):
    def minimumSize(self, nums, maxOperations):
        """
        :type nums: List[int]
        :type maxOperations: int
        :rtype: int
        """
        left = 1
        right  = max(nums)

        def find(d):
            op = 0
            for s in nums:
                op += (s-1) // d
            return op
        
        while left < right:
            mid = (left+right) // 2
            val = find(mid)
           
            if val > maxOperations:
                left = mid + 1
            else:
                right = mid 
        return left