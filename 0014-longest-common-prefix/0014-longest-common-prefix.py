class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        n = len(strs)
        prefix = strs[0]
        for i in range(1, n):
            if len(prefix) == 0:
                return ""

            idx = min(len(prefix), len(strs[i]))
            s1 = 0
            while s1 < idx:
                if prefix[s1] == strs[i][s1]:
                    s1 += 1
                else:
                    break
            prefix = prefix[:s1]
        return prefix            
