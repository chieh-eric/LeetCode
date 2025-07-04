from collections import defaultdict
class Solution(object):
    def balancedString(self, s):
        """
        :type s: str
        :rtype: int
        """
        letter = defaultdict(int)
        contain = defaultdict(int)
        cur = defaultdict(int)
        for ch in s:
            letter[ch] += 1
        n = len(s)
        avg = n // 4

        
        for key in letter:
            if letter[key] > avg:
                contain[key] = letter[key] - avg
        #print(contain)
        if not contain:
            return 0

        left = 0
        min_length = float('inf')
        for right in range(n):
            cur[s[right]] += 1
            #print(cur)
            while left < right and all(cur[key] >= contain[key] for key in contain):
                if all(cur[key] >= contain[key] for key in contain):
                    min_length = min(min_length, right-left+1)
                cur[s[left]] -= 1
                left += 1
            
            if all(cur[key] >= contain[key] for key in contain):
                min_length = min(min_length, right-left+1)

        return min_length