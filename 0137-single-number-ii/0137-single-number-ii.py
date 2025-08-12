class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0

        for i in range(32):

            bit_sum = 0

            for num in nums:
                if (num >> i) & 1:
                    bit_sum += 1
            
            if bit_sum % 3:
                if i == 31:
                    res -= (1<<31)
                
                else:
                    res |= (1<<i)
        return res
