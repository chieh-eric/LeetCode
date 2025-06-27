class Solution(object):
    def lengthAfterTransformations(self, s, t):
        """
        :type s: str
        :type t: int
        :rtype: int
        """
        mod = 10**9 + 7

        arr = [0]*26
        for ch in s:
            arr[ord(ch)-ord('a')] += 1
        
        for i in range(t):
            times = arr[-1]
            if not times:
                arr = [arr[-1]] + arr[:25]
            else:
                arr = [0] + arr[:25]
                arr[0] += times
                arr[1] += times
        return sum(arr) % mod

   