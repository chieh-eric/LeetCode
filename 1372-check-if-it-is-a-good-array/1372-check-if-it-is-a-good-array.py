class Solution(object):
    def isGoodArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def gcd(a,b):
            while b:
                a, b = b, a % b
            return a
        g = nums[0]
        for num in nums[1:]:
            g = gcd(g,num)

        if g == 1:
            return True
        return False