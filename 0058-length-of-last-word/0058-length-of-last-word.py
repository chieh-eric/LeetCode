class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = s.split(" ")
        r = []
        for num in res:
            if num:
                r.append(num)
        return len(r[-1])