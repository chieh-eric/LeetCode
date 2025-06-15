class Solution(object):
    def countDistinct(self, nums, k, p):
        """
        :type nums: List[int]
        :type k: int
        :type p: int
        :rtype: int
        """
        valid = set()

        n = len(nums)
        count = 0
        for i in range(n):
            cur = 0
            sub = []
            for j in range(i,n):
                if nums[j] % p == 0:
                    cur += 1
                if cur > k:
                    break
                sub.append(nums[j])
                if tuple(sub) not in valid:
                    valid.add(tuple(sub))
                    count += 1
        return count