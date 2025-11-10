class Solution(object):
    def maxRepOpt1(self, text):
        """
        :type text: str
        :rtype: int
        """
        # Outer loop, iterate from a - z
        # Inner loop, linear scan of sliding window ->  tolerant one difference

        n = len(text)
        count = Counter(text)
        max_len = 0

        for ch in count:
            left = 0
            tolerant = 0
            max_count = count[ch]
            for right in range(n):
                if text[right] != ch:
                    tolerant += 1
                
                if tolerant <= 1:
                    max_len = max(max_len, right - left + 1)
                    if  right - left + 1 == max_count:
                        break
                while tolerant > 1:
                    # abbaa
                    if text[left] != ch:
                        tolerant -= 1
                    left += 1
        return max_len




