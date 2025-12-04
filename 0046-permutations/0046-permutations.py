class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        n = len(nums)
        used = [False]*n
        def dfs(path, count):
            if count == n:
                res.append(path[::])
                return
            
            for i in range(n):
                if not used[i]:
                    path = path + [nums[i]]
                    used[i] = True
                    dfs(path, count+1)
                    used[i] = False
                    path.pop()
        dfs([], 0)
        return res
        