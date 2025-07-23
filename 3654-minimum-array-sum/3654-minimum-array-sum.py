class Solution(object):
    def minArraySum(self, nums, k, op1, op2):
        """
        :type nums: List[int]
        :type k: int
        :type op1: int
        :type op2: int
        :rtype: int
        """
        n = len(nums)
        used = [False]*n
        memo = {}
        # dp means the maximum sum of this array
        def dp(index, remain_op1, remain_op2):
            if index == n :
                return 0
            if (index, remain_op1, remain_op2) in memo:
                return memo[(index, remain_op1, remain_op2)]

            min_val = dp(index+1,remain_op1,remain_op2) + nums[index]
            if remain_op1 > 0:
                min_val = min(min_val,dp(index+1,remain_op1-1,remain_op2)+ (nums[index] + 1) // 2)

            if remain_op2 > 0 and nums[index] >= k:
              
                min_val = min(min_val,dp(index+1,remain_op1,remain_op2-1)+ nums[index] - k)
            
            if remain_op1 > 0 and remain_op2 > 0 and nums[index] >= k:

                temp = (nums[index] + 1) // 2
                if temp >= k:
                    min_val = min(min_val,dp(index+1,remain_op1-1,remain_op2-1)+temp-k)

                temp = nums[index] - k
                
                min_val = min(min_val,dp(index+1,remain_op1-1,remain_op2-1)+(temp + 1) // 2)
            memo[(index, remain_op1, remain_op2)] = min_val
            return min_val



        return dp(0,op1,op2)