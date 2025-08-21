class Solution(object):
    def subarrayBitwiseORs(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        
        cur = set()
        res = set()
        for num in arr:
            new = {num} | {num | x for x in cur}
            cur = new
            res |= cur
        return len(res)