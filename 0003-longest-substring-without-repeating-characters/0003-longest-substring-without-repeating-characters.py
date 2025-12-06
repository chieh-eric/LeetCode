class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        n = len(s)
        visited = set()
        max_len = 0
        for i in range(n):
            while s[i] in visited:
                visited.remove(s[left])
                left += 1
            visited.add(s[i])
            max_len = max(max_len, i - left + 1)
        return max_len
        