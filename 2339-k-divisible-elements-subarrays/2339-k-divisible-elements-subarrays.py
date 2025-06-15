class Solution(object):
    def countDistinct(self, nums, k, p):
        """
        :type nums: List[int]
        :type k: int
        :type p: int
        :rtype: int
        """
        valid = set()
        divisible = {}
        for i in nums:
            if i%p == 0:
                divisible[i] = True

        n = len(nums)
        count = 0
        for i in range(n):
            cur = 0
            for j in range(i+1,n+1):
                cur = cur + 1 if nums[j-1] in divisible else cur
                if cur > k:
                    break
                substr = ''.join(str(nums[i:j]))
                if substr not in valid:
                    valid.add(substr)
                    count += 1
        return count