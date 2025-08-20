class Solution(object):
    def countMaxOrSubsets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_val = 0
        for num in nums:
            max_val |= num
        #print(max_val) 
        
        n = len(nums)
        self.count = 0
        def backtrack(index, val):
            #print(val)
            if index == n:
                return 
            new_val = val|nums[index]
            if new_val == max_val:
                self.count += 1
            
            backtrack(index+1, new_val)
            backtrack(index+1, val)
        backtrack(0,0)
        return self.count