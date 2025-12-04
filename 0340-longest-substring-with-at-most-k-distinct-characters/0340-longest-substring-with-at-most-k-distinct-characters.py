from collections import defaultdict
class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # distinct 
        max_len = 0
        left = 0
        distinct = 0
        window = defaultdict(int)
        for i, ch in enumerate(s):
            if ch not in window:
                distinct += 1
            window[ch] += 1

            while distinct > k:
                window[s[left]] -= 1
                if window[s[left]] == 0:
                    distinct -= 1
                    del  window[s[left]]
                left += 1
            
            max_len = max(max_len, i - left + 1)
        return max_len
            
            


        