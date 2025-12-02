class Solution(object):
    def longestCommonPrefix(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: int
        """
        arr1 = Counter(arr1)
        arr2 = Counter(arr2)
        all_prfix = {}
        for key in arr1:
            s = str(key)
            for i in range(1,len(s)+1):
                all_prfix[s[:i]] = True
        
        longest = 0
        for key in arr2:
            s = str(key)
            for i in range(1,len(s)+1):
                if s[:i] in all_prfix:
                    longest = max(longest, i)
        return longest
