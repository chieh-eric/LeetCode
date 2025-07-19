class Solution(object):
    def specialPerm(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        memo = {}
        mod = 10**9 + 7
        def dfs(last_index, mask):
            if mask == (1<<n) - 1:
                return 1
            
            if (last_index,mask) in memo:
                return memo[(last_index,mask)]
            ans = 0

            for i in range(n):
                if ((mask & (1 << i)) == 0) and (nums[last_index] % nums[i] == 0 or nums[i] % nums[last_index] == 0):
                    new_mask = mask | (1 << i)
                    ans += dfs(i,new_mask)
            memo[(last_index,mask)] = ans

            return ans
        
        cumu = 0
        for i in range(n):
            cumu += dfs(i, 1 << i)
        return cumu % mod