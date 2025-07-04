class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def find_max(val):
            max_d = 1
            for i in range(2,int(val**(0.5))+1,1):
                if not val % i:
                    max_d = val // i
                    break
            return max_d
        
        count = 0
        n = len(nums)
        for i in range(n-2,-1,-1):
            while nums[i] > nums[i+1]:
                large = find_max(nums[i])
                if large == 1:
                    return -1
                count += 1
                nums[i] = nums[i] // large
        return count