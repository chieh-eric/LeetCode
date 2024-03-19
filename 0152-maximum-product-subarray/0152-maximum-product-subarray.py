class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        max_num = nums[0]
        min_num = nums[0]
        
        result = max_num
        for i in range (1,len(nums)):
            temp = max(nums[i],max_num*nums[i],min_num*nums[i])
            min_num = min(nums[i],max_num*nums[i],min_num*nums[i])
            max_num = temp
            
            result = max(max_num,result)
        return result

            