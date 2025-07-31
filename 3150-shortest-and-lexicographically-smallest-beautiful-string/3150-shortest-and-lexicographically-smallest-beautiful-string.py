class Solution(object):
    def shortestBeautifulSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        n = len(s)
        
        left = 0
        res_str = ""
        res_len = float('inf')
        count = Counter()

        for right in range(n):
            count[s[right]] += 1

            
            while "1" in count and count["1"] > k:
                if s[left] == "1":
                    count["1"] -= 1
                left += 1
            
            while left < n and s[left] == "0":
                left += 1

            
            if "1" in count and count["1"] ==  k and (right - left + 1) < res_len:
                
                if not res_str or int(res_str) > int(s[left:right+1]):
                    res_str = s[left:right+1]
        return res_str