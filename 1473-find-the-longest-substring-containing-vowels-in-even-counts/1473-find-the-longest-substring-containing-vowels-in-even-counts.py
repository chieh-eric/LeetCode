from collections import defaultdict
class Solution(object):
    def findTheLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        letter = {"a":0,"e":1,"i":2,"o":3,"u":4}

        max_len = 0
        state = 0
        pos = {0:-1}
        for i, ch in enumerate(s):
            new_state = 0
            if ch in letter:
                state = state^(1<<letter[ch])

            if state in pos:
                max_len = max(max_len,i-pos[state])
            else:
                pos[state] = i
        return max_len