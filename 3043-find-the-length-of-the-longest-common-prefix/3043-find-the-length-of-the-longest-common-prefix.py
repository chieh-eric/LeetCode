class Solution(object):
    def longestCommonPrefix(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: int
        """
        prefix_arr1 = set()

        for val in arr1:
            s = str(val)
            for i in range(1,len(s)+1):
                prefix_arr1.add(s[:i])
        
        ans = 0

        for val in arr2:
            s = str(val)
            for i in range(1, len(s)+1):
                if s[:i] in prefix_arr1:
                    ans = max(ans, i)
        return ans

