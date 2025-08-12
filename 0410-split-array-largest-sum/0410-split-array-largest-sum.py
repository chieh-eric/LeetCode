class Solution(object):
    def splitArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        total = sum(nums)
        if k == 1:
            return total

        n = len(nums)
        def calculate(val):
            split = 0
            i = 0
            while i < n:
                cur = 0
                while i < n and cur <= val:
                    cur += nums[i]
                    i += 1
                
                if cur > val:
                    cur -= nums[i-1]
                    i -= 1
                
                split += 1
                #print(cur)
                if split > k:
                    return False
            return True

        left = 0
        right = total
       
        while left < right:
            mid = (left+right) // 2
            res = calculate(mid)
            if not res:
                left = mid + 1
            else:
                right = mid

        return left