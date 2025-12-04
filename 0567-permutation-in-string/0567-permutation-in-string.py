from collections import defaultdict
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        count = Counter(s1)
        expect = len(count)
        window = defaultdict(int)

        n = len(s2)
        m = len(s1)
        left = 0
        good = 0
        for i in range(n):
            if i - left + 1 > m:
                if s2[left] in count and window[s2[left]] == count[s2[left]]:
                    good -= 1
                window[s2[left]] -= 1
                left += 1
            window[s2[i]] += 1
            if s2[i] in count and count[s2[i]] == window[s2[i]]:
                good += 1
            if good == expect:
                return True

        return False
                

