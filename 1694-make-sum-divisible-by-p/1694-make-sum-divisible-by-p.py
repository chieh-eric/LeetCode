class Solution(object):
    def minSubarray(self, nums, p):
        """
        :type nums: List[int]
        :type p: int
        :rtype: int
        """
        prefix = 0
        rem = sum(nums) % p
        min_length = float('inf')
        if rem == 0:
            return 0
        dic = {0:-1}


        for i, num in enumerate(nums):
            prefix = (prefix+num) % p
            target = (prefix - rem + p) % p
            if target in dic:
                min_length = min(min_length, i - dic[target])
            dic[prefix] = i
        
        return min_length if min_length < len(nums) else -1
        ##print(prefix)
        # (prefix[j] - prefix[i]) % p == rem
        # (prefix[j] - rem + p ) % p = prefix[i] % p