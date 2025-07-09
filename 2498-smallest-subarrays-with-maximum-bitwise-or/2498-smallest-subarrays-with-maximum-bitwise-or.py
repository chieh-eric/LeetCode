class Solution(object):
    def smallestSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        digit = {}
        last_num = nums[-1]
        shift = 0
        while last_num: 
            d = last_num & 1
            if d:
                digit[d*(2**shift)] = n - 1
            shift += 1
            last_num >>= 1

        res = [0]*n
        res[n-1] = 1
        for i in range(n-2,-1,-1):
            num = nums[i]
            shift = 0
            #print(digit)
            while num: 
                d = num & 1
                if d:
                    digit[d*(2**shift)] = i
                shift += 1
                num >>= 1
            if not digit:
                res[i] = 1
            else:
                res[i] = max(digit.values()) - i + 1 

        return res
        #print(res)
        #print(digit)
