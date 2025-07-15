class Solution(object):
    def splitArraySameAverage(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        total = sum(nums)
        n = len(nums)

        memo = {}
        def dfs(i,k,target):
            if k == 0:
                return target == 0
            if (i,k,target) in memo:
                return memo[(i,k,target)]
            for j in range(i,len(nums)-k+1):
                if dfs(j+1,k-1,target-nums[j]):
                    memo[(j+1,k-1,target-nums[j])] = True
                    return True
            memo[(i,k,target)] = False
            return False


        for i in range(1,n//2+1):
            if total*i % n != 0:
                continue
            t = total*i / n
            if dfs(0,i,t):
                return True
        return False