from collections import defaultdict
class Solution(object):
    def longestIdealString(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # count, use for storing the maximum length end in this character
        # Outer loop will iterate the s
        # Inner for loop will iterate, cur a-> , k = 3,

        # count[a] = 1, count[c] = 2, count[f] = 1, count[g] = 2, count[b] = 3, count[d] = 4

        count = defaultdict(int)
        min_char_value = ord('a')
        max_char_value = ord('z')

        for ch in s:
            start = ord(ch) - k
            max_val = 0 
            for i in range(2*k+1):
                if min_char_value <= start + i <= max_char_value:
                    max_val = max(max_val, count[chr(start + i)])
            count[ch] = max_val + 1
        ans = 0
        for ch in count:
            ans = max(ans, count[ch])
        return ans



